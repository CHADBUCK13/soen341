from audioop import ratecv
from unicodedata import category
from urllib.error import HTTPError
from firebase_admin import firestore
import json
from requests.exceptions import HTTPError
from ecommerce.models.items import Item
from ecommerce.models.items import Category
from ecommerce.models.items import Rating

db = firestore.client()

items_ref=db.collection(u'items')

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
    
        return item_collection_to_dict(allItemsRef)
    
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
    
    item_dict = items_ref.document(itemID).to_dict()
    return item_from_dict(item_dict)

def item_from_dict(item_dict):

    category = Category(item_dict['category']['category_name'], item_dict['category']['relatedcategory'])
    return Item(item_dict['name'],item_dict['sellerID'],item_dict['photo'],item_dict['price'],item_dict['description'],item_dict['weight'],item_dict['rating']['score'],item_dict['rating']['numberofreviews'],item_dict['sales'],category)


def item_collection_to_dict(collection):
    allItems = []

    for itemDoc in collection:
        dict = itemDoc.to_dict()
        item = item_from_dict(dict)
    
       
        allItems.append(item)

    return allItems
    