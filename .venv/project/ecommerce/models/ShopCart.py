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
    

class ShoppingCart():

    def __init__(self,email,cartItems=[]):
        self.email=email
        self.cartItems=cartItems

    




class orderItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} of {self.item.name}"

    def get_total_item_price(self):
        return self.quantity * self.item.price

    # def get_total_discount_item_price(self):
    #     return self.quantity * self.item.discount_price

    # def get_amount_saved(self):
    #     return self.get_total_item_price() - self.get_total_discount_item_price()

    def get_final_price(self):
        if self.item.discount_price:
            return self.get_total_discount_item_price()
        return self.get_total_item_price()

class order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    ref_code = models.CharField(max_length=20, blank=True, null=True)
    items = models.ManyToManyField(orderItem) 
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)
    shipping_address = models.ForeignKey(
        'Address', related_name='shipping_address', on_delete=models.SET_NULL, blank=True, null=True)
    billing_address = models.ForeignKey(##
        'Address', related_name='billing_address', on_delete=models.SET_NULL, blank=True, null=True)
    payment = models.ForeignKey(##
        'Payment', on_delete=models.SET_NULL, blank=True, null=True)
    coupon = models.ForeignKey(
        'Coupon', on_delete=models.SET_NULL, blank=True, null=True)
    being_delivered = models.BooleanField(default=False)
    received = models.BooleanField(default=False)


class Address(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    street_address = models.CharField(max_length=100)
    apartment_address = models.CharField(max_length=100)
    #country = country(multiple=False)
    zip = models.CharField(max_length=100)
    #address_type = models.CharField(max_length=1, choices=ADDRESS_CHOICES)
    default = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

# class Coupon(models.Model):
#     code = models.CharField(max_length=15)
#     amount = models.FloatField()

#     def __str__(self):
#         return self.code

#Class refund?

#Class payment?
    
