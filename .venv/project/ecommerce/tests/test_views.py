
import os
from time import sleep
from ..databaseContext import DatabaseContext
from django.test import TestCase
from django.urls import reverse
from ..models.buyer import Buyer
from ..models.seller import Seller
from ..controllers.forms.signupForm import BuyerSignupForm, SellerSignupForm
from ..controllers.itemBrowsing.itemBrowsingViews import addItem, searchItems
from ..views import home


class TestLogin(TestCase):

    def test_login_page_response_code(self):
        url = reverse("login")
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'register.html')


class TestSignup(TestCase):

    def test_signup_buyer_page_response_code(self):
        url = reverse("signupBuyer")
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'signup.html')

    def test_signup_seller_page_response_code(self):
        url = reverse("signupSeller")
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'signup.html')
        self.assertEqual(response.status_code, 200)


class TestLogout(TestCase):

    def test_logout_response_code(self):
        url = reverse("logout")
        response = self.client.get(url)

        self.assertEqual(response.status_code, 302)


class Testhome(TestCase):
    def setUp(self):
        self.session = self.client.session
        self.session['is_logged_in'] = False
        self.categorySearch = "Games"

    def test_home_response_code(self):
        url = reverse("home")
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'home.html')
        self.assertEqual(response.status_code, 200)

    def test_logged_in_response(self):
        self.assertFalse(self.session['is_logged_in'])


class TestItemBrowsingViews(TestCase):
    def setUp(self):
        self.session = self.client.session
        self.session['is_logged_in'] = False
        self.categorySearch = "Games"

    def test_addItem_response_code(self):
        url = reverse("addItem")
        response = self.client.get(url)

        self.assertTemplateUsed(response, 'addItem.html')
        self.assertEqual(response.status_code, 200)

        self.assertTemplateUsed(response, 'addItem.html')
        self.assertEqual(response.status_code, 200)

    def test_searchItem_response_code(self):
        url = reverse("searchItems")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
