from django.db import models
from django.conf import settings
from .items import Item



class CartItem():

    def __init__(self,itemID, quantity=1):
        self.id = itemID
        self.quantity = quantity
    
    def quantityDown(self):
        if self.quantity > 0:
            self.quantity = self.quantity-1

    def quantityUp(self):
        self.quantity = self.quantity+1

    def setQuantity(self,quantity):
        if quantity>0:
            self.quantity = quantity
    

class shopping_cart():

    def __init__(self,email,cartItems=[]):
        self.email=email
        self.cartItems=cartItems

    
