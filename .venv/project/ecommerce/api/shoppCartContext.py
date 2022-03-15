from firebase_admin import firestore
from ..models.shopCart import ShoppingCart


db = firestore.client()

#reference to items collections
sc_ref=db.collection(u'shoppingCarts')

def getShoppingCart(email):
    """
    Gets a Shopping Cart from the DB.
    """
    sc = sc_ref.where(u'email',u'==',email).stream()
    
    scDict = sc.to_dict()
    print(scDict)

    return scDict

def saveShoppingCart(email, cartItems=[]):
    """
    Saves a Shopping Cart to the DB.
    """
    
    sc = {
        'email':email,
        'cartItems':cartItems
    }

    print(sc)

    sc_ref.document(email).set(sc)