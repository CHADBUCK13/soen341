"""this module contains the test for the forms: buyer signup,
seller sign up, item, login and reset password forms
"""
from django.test import TestCase
from ..controllers.forms.signupForm import BuyerSignupForm, SellerSignupForm
from ..controllers.forms.loginForm import LoginForm
from ..controllers.forms.resetPasswordForm import ResetPasswordForm
from ..controllers.forms.itemForm import ItemForm
from ..controllers.forms.bankingForm import BankingBuyerForm, BankingSellerForm


class TestFrorms(TestCase):
    """contains tests for forms
    """

    def test_buyer_sign_up_form_valid_data(self):
        """test if the buyer sign up/;  form is valid using valid data
        """
        buyer_signup_from = BuyerSignupForm(data={
            "email": 'matintavak@yahoo.com',
            "password1": '123*pass',
            "password2": '123*pass',
            "firstname": 'name',
            "lastname": 'surname',
            "country": 'aCountry',
            "city": 'aCity',
            "address": 'anAddress',
            "postal_code": 'aCode',
            "date_of_birth": '1/01/1222'
        })
        self.assertTrue(buyer_signup_from.is_valid())

    def test_buyer_sign_up_form_invalid_data(self):
        """test if the buyer sign up form is invalid with invalid data
        """
        buyer_signup_from = BuyerSignupForm(data={})
        self.assertFalse(buyer_signup_from.is_valid())
        self.assertEqual(len(buyer_signup_from.errors), 10)

    def test_seller_sign_up_form_valid_data(self):
        """test if the seller sign up form is valid using valid data
        """
        seller_signup_from = SellerSignupForm(data={
            "email": 'matintavak@yahoo.com',
            "password1": '123*pass',
            "password2": '123*pass',
            "name": 'name',
            "country": 'aCountry',
            "city": 'aCity',
            "address": 'anAddress',
            "postal_code": 'aCode',
            "service_number": 'aNumber'
        })
        self.assertTrue(seller_signup_from.is_valid())

    def test_seller_sign_up_form_invalid_data(self):
        """test if the seller sign up form is invalid with invalid data
        """
        seller_signup_from = SellerSignupForm(data={})
        self.assertFalse(seller_signup_from.is_valid())
        self.assertEqual(len(seller_signup_from.errors), 9)

    def test_login_form_valid_data(self):
        """test if the login form is valid using valid data
        """
        login_form = LoginForm(data={
            'email': 'anEmail@email.com',
            'password': "aPassword"
        })
        self.assertTrue(login_form.is_valid())

    def test_login_form_invalid_data(self):
        """test if the login form is invalid with invalid data
        """
        login_form = LoginForm(data={})
        self.assertFalse(login_form.is_valid())

    def test_reset_password_form_valid_data(self):
        """test if the reset password form is valid with valid data
        """
        reset_form = ResetPasswordForm(data={
            'email': 'user@email.com',
        })
        self.assertTrue(reset_form.is_valid())

    def test_item_form_invalid_data(self):
        """test if the item form is invalid with an invalid image
        """
        item_form = ItemForm(data={
            'name': 'itemName',
            'price': '123',
            'description': 'ItemDescription',
            'weight': 'aWeight',
            'category': 'aCategory',
            'relatedCategories': 'Categories',
            'image': 'anAddress',
        })
        self.assertFalse(item_form.is_valid())

    def test_banking_seller_form_valid_data(self):
        """Test if the form is valid if we provide valid banking details
        """
        seller_form = BankingSellerForm(data={
            'transit': 'trans',
            'institution': '123',
            'account': 'account',
        })
        self.assertTrue(seller_form.is_valid())

    def test_banking_seller_form_invalid_data(self):
        """Test if the form is valid if we provide wrong banking details
        """
        seller_form = BankingSellerForm(data={
            'transit': 'wrongtransitNumber',
            'institution': '123',
            'account': 'account',
        })
        self.assertFalse(seller_form.is_valid())
