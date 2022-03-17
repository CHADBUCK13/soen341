from urllib.error import HTTPError
from firebase_admin import firestore
import json
from requests.exceptions import HTTPError
from .itembrowsing import get_item_by_ID
from ..models.items import Item


db = firestore.client()

items_ref=db.collection(u'items')


def add_item_to_cart(email, itemId, quantity):
    """
    adding items to cart
    """
    #collection shopping_cart contains subcollections of emails that each contain a a document itemId
    
    try:
        cart_ref = db.collection(u'shopping_cart').document(email)
        if cart_ref.get().exists:
            cart_data = {'items.'+ itemId: quantity}
            cart_ref.update(cart_data)

        else:
            cart_data = {'items': {itemId: quantity}}
            cart_ref.set(cart_data)

        return True
 

    except HTTPError as e:
            return json.loads(e.strerror)


def get_items_from_cart(email):
    """
    from email find items in item database with same itemID, return collection of items with all information
    """

    shopping_cart_ref = db.collection(u'shopping_cart').document(email).get()
    try:
        
        return shopping_cart_to_dict(shopping_cart_ref)

    except HTTPError as e:
            return json.loads(e.strerror)


def shopping_cart_to_dict(cart_document):
    allItems = []
  
    cart=cart_document.to_dict()['items']


    for itemID in cart:
        item = get_item_by_ID(itemID)
        quantity = cart[itemID]
        allItems.append([item,quantity])

    return allItems


    
def delete_items_from_cart(email, itemId):
    """
    delete item 
    """
    try:
        shopping_cart_ref = db.collection(u'shopping_cart').document(email)
        shopping_cart_ref.get()
        shopping_cart_ref.update({'items.'+itemId: firestore.DELETE_FIELD})
        
        return True
 
    except HTTPError as e:
            return json.loads(e.strerror)



def update_item_quantity(email, itemId, quantity):

    if (quantity<0):
        return False

    try:
        item_ref = db.collection(u'shopping_cart').document(email)
        item_ref.update({'items.'+itemId: quantity})

    except HTTPError as e:
            return json.loads(e.strerror)


def create_cart(email):

    try:
        cart_ref = db.collection(u'shopping_cart').document(email)
        if cart_ref.get().exists:
            return False

        else:
            cart_ref.set({'items':{}})

        return True
 

    except HTTPError as e:
        return json.loads(e.strerror)