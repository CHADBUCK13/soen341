from django.test import TestCase
from ..controllers.forms.signupForm import BuyerSignupForm, SellerSignupForm
from ..controllers.forms.loginForm import LoginForm


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