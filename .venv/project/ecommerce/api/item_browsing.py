from urllib.error import HTTPError
import json
from firebase_admin import firestore
from django.forms.models import model_to_dict
from requests.exceptions import HTTPError
from ..models.items import Item

db = firestore.client()

items_ref=db.collection('items')

def add_items(item:Item):
    """
    adding items
    """
    items_data = {
        'name':item.name,
        'seller_id':item.seller_id,
        'photo':item.photo,
        'price':item.price,
        'description':item.description,
        'weight':item.weight,
        'sales':item.sales,
        'rating': {
            'score':item.score,
            'numberofreviews':0
            },
        'category': {
            'category_name' : item.category.category_name,
            'relatedcategory': item.category.related_categories
        }
    }

    items_ref.add(items_data)

def order_by_price(min_price=0, max_price=0):
    """
    search for items based on price range
    """
    try:

        price_ref=items_ref.where('price','>',min_price).where('price','<',max_price)
        ordered_price_ref = price_ref.order_by('price').stream()
        
        return item_collection_to_dict(ordered_price_ref)

    except HTTPError as error:
        return json.loads(error.strerror)


def better_than_score(score):
    """
    get items with a given score
    """
    try:

        itemsreviewed=items_ref.where('score', '<=', score).stream()

        return item_collection_to_dict(itemsreviewed)

    except HTTPError as error:
        return json.loads(error.strerror)


def worse_than_score(score):
    """
    get descending order for items
    """

    try:

        itemsreviewed=items_ref.where('score', '>', score).stream()

        return item_collection_to_dict(itemsreviewed)

    except HTTPError as error:
        return json.loads(error.strerror)


def get_categories():
    """
    get all categories
    """
    try:
        category_names_ref=db.collection('Categories').document('names')
        category_names_dict = category_names_ref.get().to_dict()
        return category_names_dict['names']

    except HTTPError as error:
        return json.loads(error.strerror)


def get_all_items(number_of_items = 0):
    """
    getting all items
    """
    try:
        all_items_ref = items_ref.stream()
        all_items:list = item_collection_to_dict(all_items_ref)
        return all_items

    except HTTPError as error:
        return json.loads(error.strerror)


def get_all_items_dict(number_of_items = 0):
    """
    get items as a dictionnay
    """
    try:
        all_items_ref = items_ref.stream()
        all_items = []

        for item_doc in all_items_ref:
            item_dict = item_doc.to_dict()
            item_id = item_doc.id
            item_dict['id'] = item_id
            all_items.append(item_dict)

        return all_items

    except HTTPError as error:
        return json.loads(error.strerror)


def get_items_by_category(category = "", number_of_items=0):
    """
    get items by category
    """
    try:
        new_items_ref = items_ref.where('category.category_name', '==', category).limit(number_of_items).stream()        
        return item_collection_to_dict(new_items_ref)

    except HTTPError as error:
        return json.loads(error.strerror)

def get_items_on_sale(number_of_items):
    """
    get all items with a certain number of sales
    """

    try:
        new_items_ref = items_ref.where('sales', '==', True).limit(number_of_items).stream()
       
        return item_collection_to_dict(new_items_ref)

    except HTTPError as error:
        return json.loads(error.strerror)

def get_item_by_id(item_id):
    """
    get items by their id
    """
    item_id_ref = items_ref.document(item_id).get()
    item_dict = item_id_ref.to_dict()
    item_dict['id']=item_id
    return Item(item_data= item_dict)

def get_items_by_search(search_text=""):
    """
    Gets all Items that match (or are similar) to the given Search Text.
    """

    searched_items_ref = items_ref.stream()
    searched_items = []

    for item_doc in searched_items_ref:
        item_dict = item_doc.to_dict()
        item_id = item_doc.id
        item_dict['id'] = item_id
        item = Item(item_data=item_dict)
        if item.match(search_text=search_text):
            searched_items.append(item)
    
    return searched_items


#Helper functions


def item_collection_to_dict(collection):
    """
    save item collection as a dictionnary
    """
    all_items = []

    for item_doc in collection:
        item_dict = item_doc.to_dict()
        item_id = item_doc.id
        item_dict['id'] = item_id
        item = Item(item_data=item_dict)
        
        all_items.append(item)

    return all_items