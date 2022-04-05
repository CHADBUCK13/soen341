from django.test import TestCase
from django.urls import reverse
from  .. import models
from  ecommerce.models.buyer  import Buyer
from  ecommerce.models.seller  import Seller
from  ecommerce.models.user  import User
from ..controllers.forms.signupForm import BuyerSignupForm, SellerSignupForm


class TestBuyerModel(TestCase):

    def test_accountType(self):
        self.assertEquals(Buyer.accountType(self),"buyer")


class TestSellerModel(TestCase):
    
    def test_accountType(self):
        self.assertEquals(Seller.accountType(self),"seller")
