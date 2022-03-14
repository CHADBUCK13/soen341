from ecommerce.models.items import Item
from django.conf import settings
from decimal import Decimal
from firebase_admin import db
import json
from requests.exceptions import HTTPError

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

    
#create a shopping cart
def init(self, request):
        try:
            self.session = request.session
            cart = self.session.get(settings.CART_SESSION_ID)
            if not cart:
                cart = self.session[settings.CART_SEESION_ID] = {}
            self.cart = cart

        except HTTPError as e:
            return json.loads(e.strerror)

#add an item to the shopping cart
def add(self, Item, quantity=1, updateQuantity= False):
        try:
            item_id = str(Item.id)
            if item_id not in self.cart:
                self.cart[item_id] = {'quantity': 0,
                                    'price': str(Item.price)}

            if updateQuantity:
                self.cart[item_id]['quantity'] = quantity
            else:
                self.cart[item_id]['quantity'] += quantity
                self.save()

        except HTTPError as e:
            return json.loads(e.strerror)

#save your shopping cart
def save(self):
        try:

            self.session[settings.CART_SESSION_ID] = self.cart
            self.session.modified = True

        except HTTPError as e:
            return json.loads(e.strerror)

#remove a certain item from the shooping cart
#item will be removed throughly regarless of its quantity's 
def remove(self, item):
        try:
            item_id = str(Item.id)
            if item_id in self.cart:
                del self.cart[item_id]
                self.save()

        except HTTPError as e:
            return json.loads(e.strerror)

#edit the quantity of a certain item in the shopping cart
    #def edit (self):

#get the total price of the shopping cart
def get_total_price(self):
        try:

            return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())

        except HTTPError as e:
            return json.loads(e.strerror)

#clear the shopping cart of every item in it
def clear(self):
        try:

            del self.session[settings.CART_SESSION_ID]
            self.session.modified = True

        except HTTPError as e:
            return json.loads(e.strerror)



    
def add_item_to_cart(itemId, quantity, email):

            data = {
                u'itemID': itemId,
                u'quantity': quantity
            }

db.collection(u'email').document(u'itemId')