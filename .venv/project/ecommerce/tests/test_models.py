from django.test import TestCase
from django.urls import reverse
from  .. import models
from  ecommerce.models.buyer  import Buyer
from  ecommerce.models.seller  import Seller
from  ecommerce.models.user  import User
from ..controllers.forms.signup_form import BuyerSignupForm, SellerSignupForm


class TestBuyerModel(TestCase):

    def test_accountType(self):
        self.assertEqual(Buyer.account_type(self),"buyer")


class TestSellerModel(TestCase):
    
    def test_accountType(self):
        self.assertEqual(Seller.account_type(self),"seller")
