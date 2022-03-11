from django.test import TestCase
from django.urls import reverse
from  .. import models
from  ..models.buyer  import Buyer
from  ..models.seller  import Seller
from  ..models.user  import User
from model_mommy import mommy
from ..controllers.forms.signupForm import BuyerSignupForm, SellerSignupForm


class TestBuyerModel(TestCase):
    def setUp(self):
         self.buyer1= mommy.make('models.buyer')
        
    def test_signUp(self):
        
        self.assertTrue(isinstance(self.buyer1, Buyer))
  
        
        
    
    def test_accountType(self):
        self.assertEquals(Buyer.accountType(self),"buyer")


class TestSellerModel(TestCase):
    
    def test_accountType(self):
        self.assertEquals(Seller.accountType(self),"seller")

    
           