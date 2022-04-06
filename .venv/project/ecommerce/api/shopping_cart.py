from urllib.error import HTTPError
import json
from firebase_admin import firestore
from google.cloud import firestore as fs
from requests.exceptions import HTTPError
from .item_browsing import get_item_by_id
from ecommerce.models.items import Item


db = firestore.client()

items_ref=db.collection('items')


def add_item_to_cart(email, item_id, quantity):
    """
    adding items to cart
    """
    #collection shopping_cart contains subcollections of emails that each contain a a document itemId
    
    try:
        cart_ref = db.collection('shopping_cart').document(email)
        if cart_ref.get().exists:
            cart_data = {'items.'+ item_id: quantity}
            cart_ref.update(cart_data)

        else:
            cart_data = {'items': {item_id: quantity}}
            cart_ref.set(cart_data)

        return True
 

    except HTTPError as error:
            return json.loads(error.strerror)


def get_items_from_cart(email):
    """
    from email find items in item database with same itemID, return collection of items with all information
    """

    shopping_cart_ref = db.collection('shopping_cart').document(email).get()
    try:
        
        return shopping_cart_to_dict(shopping_cart_ref)

    except HTTPError as error:
        return json.loads(error.strerror)


def shopping_cart_to_dict(cart_document):
    """
    save shopping cart collection as a dictionnary
    """
    all_items = []
  
    cart=cart_document.to_dict()['items']


    for item_id in cart:
        item = get_item_by_id(item_id)
        quantity = cart[item_id]
        all_items.append([item,quantity])

    return all_items


    
def delete_items_from_cart(email, item_id):
    """
    delete item
    """
    try:
        shopping_cart_ref = db.collection('shopping_cart').document(email)
        shopping_cart_ref.get()
        shopping_cart_ref.update({'items.'+item_id: fs.DELETE_FIELD})

        return True

    except HTTPError as error:
        return json.loads(error.strerror)



def update_item_quantity(email, item_id, quantity):
    """
    update the quantity of an item
    """
    #if quantity<0:
    #    return False

    try:
        item_ref = db.collection('shopping_cart').document(email)
        item_ref.update({'items.'+item_id: quantity})

    except HTTPError as error:
        return json.loads(error.strerror)


def create_cart(email):
    """
    create a new shopping cart
    """
    try:
        cart_ref = db.collection('shopping_cart').document(email)
        if cart_ref.get().exists:
            return False

        else:
            cart_ref.set({'items':{}})

        return True


    except HTTPError as error:
        return json.loads(error.strerror)