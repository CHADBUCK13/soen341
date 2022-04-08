"""this module contains tests for the various URLs"""
from django.test import TestCase
from django.urls import reverse, resolve
from ..views import home
from ..controllers.itemBrowsing.item_browsing_views import add_item, search_items
from ..controllers.account.account_views import login, logout, signup_buyer, signup_seller


class TestUrls(TestCase):
    """This class tests that the urls resolve to the correct place
    """

    def test_home_url_is_resolved(self):
        """test that the user home request resolves to home"""
        url = reverse("home")
        self.assertEqual(resolve(url).func, home)

    def test_login_url_is_resolved(self):
        """test that the user login request resolves to the correct page"""
        url = reverse("login")
        self.assertEqual(resolve(url).func, login)

    def test_logout_url_is_resolved(self):
        """test that the user logout request resolves to the correct page"""
        url = reverse("logout")
        self.assertEqual(resolve(url).func, logout)

    def test_signup_buyer_url_is_resolved(self):
        """test that the user singup request resolves to the correct page
            when signing up as a buyer"""
        url = reverse("signupBuyer")
        self.assertEqual(resolve(url).func, signup_buyer)

    def test_signup_seller_url_is_resolved(self):
        """test that the user signup request resolves to the correct page
        when signing up as a seller"""
        url = reverse("signupSeller")
        self.assertEqual(resolve(url).func, signup_seller)

    def test_add_item_url_is_resolved(self):
        """test that the add item request resolves to the correct page"""
        url = reverse("addItem")
        self.assertEqual(resolve(url).func, add_item)

    def test_search_items_url_is_resolved(self):
        """
        test to see if the search item request resolves to the correct page
        """
        url = reverse("searchItems")
        self.assertEqual(resolve(url).func, search_items)
