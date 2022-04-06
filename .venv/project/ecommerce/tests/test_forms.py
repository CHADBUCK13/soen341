from django.test import TestCase
from ..controllers.forms.signup_form import BuyerSignupForm, SellerSignupForm
from ..controllers.forms.login_form import LoginForm
from ..controllers.forms.reset_password_form import ResetPasswordForm
from ..controllers.forms.item_form import ItemForm


class TestFrorms(TestCase):
    
    def test_buyer_signup_form_valid_data(self):
        buyer_signup_from= BuyerSignupForm(data={
            "email": 'matintavak@yahoo.com',
            "password1" : '123*pass',
            "password2" : '123*pass',
            "firstname" : 'name',
            "lastname" : 'surname',
            "country" : 'aCountry',
            "city" :'aCity',
            "address": 'anAddress',
            "postal_code" : 'aCode',
            "date_of_birth": '1/01/1222'
        })
        self.assertTrue(buyer_signup_from.is_valid())
        
        
    def test_buyer_signup_form_inValid_data(self):
            buyer_signup_from= BuyerSignupForm(data={})
            self.assertFalse(buyer_signup_from.is_valid())
            self.assertEquals(len(buyer_signup_from.errors),10)
        
        
    def test_seller_signup_form_valid_data(self):
        seller_signup_from= SellerSignupForm(data={
            "email": 'matintavak@yahoo.com',
            "password1" : '123*pass',
            "password2" : '123*pass',
            "name" : 'name',
            "country" : 'aCountry',
            "city" :'aCity',
            "address": 'anAddress',
            "postal_code" : 'aCode',
            "service_number": 'aNumber'
        })
        self.assertTrue(seller_signup_from.is_valid())
        
    def test_seller_signup_form_inValid_data(self):
            seller_signup_from= SellerSignupForm(data={})
            self.assertFalse(seller_signup_from.is_valid())
            self.assertEquals(len(seller_signup_from.errors),9)
        
        
    def test_login_form_valid_data(self):
        login_form = LoginForm(data={
            'email' : 'anEmail@email.com',
            'password': "aPassword"  
        })
        self.assertTrue(login_form.is_valid())
        
    def test_login_form_inValid_data(self):
        login_form = LoginForm(data={})
        self.assertFalse(login_form.is_valid())
        
    def test_resetPassword_form_valid_data(self):
        reset_Form =ResetPasswordForm(data={
            'email' : 'user@email.com',
        })
        self.assertTrue(reset_Form.is_valid())
    
    def test_item_form_valid_data(self):
        Item_form= ItemForm(data={
            'name': 'itemName',
            'price' : '123',
            'description' : 'ItemDescription',
            'weight' : 'aWeight',
           'category' : 'aCategory',
            'relatedCategories' :'Categories',
           'image': 'anAddress',
        })
        print(Item_form.is_valid())