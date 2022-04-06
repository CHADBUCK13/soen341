"""
This contains all url tests
"""

from django.test import TestCase
from django.urls import reverse, resolve
from ..views import home
from ..controllers.itemBrowsing.item_browsing_views import add_item, search_items
from ..controllers.account.accountViews import login, logout, signupBuyer, signupSeller



class TestUrls(TestCase):
    """
tests for various urls
    """

    def test_home_url_is_resolved(self):
        """
        test to see if home url resolves to home.
        """
        url = reverse("home")
        self.assertEqual(resolve(url).func, home)

    def test_login_url_is_resolved(self):
        """
        test to see if login url resolves to login.
        """
        url = reverse("login")
        self.assertEqual(resolve(url).func, login)

    def test_logout_url_is_resolved(self):
        """
        test to see if logout url resolves to logout.
        """
        url = reverse("logout")
        self.assertEqual(resolve(url).func, logout)

    def test_sign_buyer_url_is_resolved(self):
        """
        test to see if the sign in buyer request resolves to the correct page
        """
        url = reverse("signupBuyer")
        self.assertEqual(resolve(url).func, signupBuyer)

    def test_signup_seller_url_is_resolved(self):
        """
        test to see if the sign in seller request resolves to the correct page
        """
        url = reverse("signupSeller")
        self.assertEqual(resolve(url).func, signupSeller)

    def test_add_item_url_is_resolved(self):
        """
        test to see if the add item request resolves to the correct page
        """
        url = reverse("addItem")
        self.assertEqual(resolve(url).func, add_item)

    def test_search_items_url_is_resolved(self):
        """
        test to see if the search item request resolves to the correct page
        """
        url = reverse("searchItems")
        self.assertEqual(resolve(url).func, search_items)
