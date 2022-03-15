from urllib.error import HTTPError
from firebase_admin import firestore
import json
from django.forms.models import model_to_dict
from requests.exceptions import HTTPError
from ..models.items import Item

db = firestore.client()

items_ref=db.collection(u'items')

def addItems(item:Item):
    items_data = {
        'name':item.name,
        'sellerID':item.sellerID,
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

def order_by_price(min=0, max=0): 
    """
    search for items based on price range
    """
    try: 
        items_ref=db.collection(u'items')
        price_ref=items_ref.where(u'price',u'>',min).where(u'price',u'<',max).order_by(u'price').stream()

        return item_collection_to_dict(price_ref)

    except HTTPError as e:
        return json.loads(e.strerror)


def better_than_score(score):
    """
    get items with a given score
    """
    try:

        items_ref=db.collection(u'items')
        itemsreviewed=items_ref.where(u'score', u'<=', score).stream()

        return item_collection_to_dict(itemsreviewed)

    except HTTPError as e:
        return json.loads(e.strerror)


def worse_than_score(score):
    """
    get descending order for items
    """

    try:

        items_ref=db.collection(u'items')
        itemsreviewed=items_ref.where(u'score', u'>', score).stream()

        return item_collection_to_dict(itemsreviewed)

    except HTTPError as e:
        return json.loads(e.strerror)


       
def get_categories():
    """
    get all categories
    """
    try:
        categoryNamesRef=db.collection(u'Categories').document(u'names')
        categoryNamesDict = categoryNamesRef.get().to_dict()
        return categoryNamesDict['names']

    except HTTPError as e:
        return json.loads(e.strerror)


def get_all_items(numberOfItems = 0):
    try:
        allItemsRef = items_ref.stream()
        allItems:list = item_collection_to_dict(allItemsRef)
        return allItems
    
    except HTTPError as e:
        return json.loads(e.strerror)


def get_all_items_dict(numberOfItems = 0):
    try:
        allItemsRef = items_ref.stream()
        allItems = []

        for itemDoc in allItemsRef:
            item_dict = itemDoc.to_dict()
        
            allItems.append(item_dict)

        return allItems
    
    except HTTPError as e:
        return json.loads(e.strerror)


def get_items_by_category(category = "", numberOfItems=0):
    try:
        itemsRef = items_ref.where(u'category', u'==', category).limit(numberOfItems).stream()        
        return item_collection_to_dict(itemsRef)

    except HTTPError as e:
        return json.loads(e.strerror)

def get_items_on_sale(numberOfItems):
    """
    get all items with a certain number of sales
    """

    try:
        itemsRef = items_ref.where(u'sales', u'==', True).limit(numberOfItems).stream()
       
        return item_collection_to_dict(itemsRef)


    except HTTPError as e:
        return json.loads(e.strerror)

def get_item_by_ID(itemID):
    
    item_ID_ref = items_ref.document(itemID).get()
    item_dict = item_ID_ref.to_dict()
    return Item(item_data= item_dict)

def get_items_by_search(searchText=""):
    """
    Gets all Items that match (or are similar) to the given Search Text.
    """

    searchedItemsRef = items_ref.stream()
    searchedItems = []

    for itemDoc in searchedItemsRef:
        item = Item(item_data=itemDoc.to_dict())
        if item.match(searchText=searchText):
            searchedItems.append(item)
    
    return searchedItems


#Helper functions


def item_collection_to_dict(collection):
    allItems = []

    for itemDoc in collection:
        item_dict = itemDoc.to_dict()
        item = Item(item_data=item_dict)
        
        allItems.append(item)

    return allItems

