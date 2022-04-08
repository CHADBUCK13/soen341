"""this module contains the tests for views.py
"""
from django.test import TestCase
from django.urls import reverse


class TestLogin(TestCase):
    """test the response code for the login request
    """

    def test_login_page_response_code(self):
        """test that the login request returns the correct staus code and response"""
        url = reverse("login")
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'register.html')


class TestSignup(TestCase):
    """test the response for buyer and seller signup requests
    """

    def test_signup_buyer_page_response_code(self):
        """test the response code for the sign up as buyer request
        """
        url = reverse("signupBuyer")
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'signup.html')

    def test_signup_seller_page_response_code(self):
        """test the response code for the sign up as seller request
        """
        url = reverse("signupSeller")
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'signup.html')
        self.assertEqual(response.status_code, 200)


class TestLogout(TestCase):
    """test the response for logout request
    """

    def test_logout_response_code(self):
        """test that the logout request returns the correct status code
        """
        url = reverse("logout")
        response = self.client.get(url)

        self.assertEqual(response.status_code, 302)


class Testhome(TestCase):
    """test that home request responses
    """
    def setUp(self):
        self.session = self.client.session
        self.session['is_logged_in'] = False
        self.category_search = "Games"

    def test_home_response_code(self):
        """test that the home request returns the correct status code
        """
        url = reverse("home")
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'home.html')
        self.assertEqual(response.status_code, 200)

    def test_logged_in_response(self):
        """test the logged in user home request"""
        self.assertFalse(self.session['is_logged_in'])


class TestItemBrowsingViews(TestCase):
    """tests for the item browsing views"""
    def setUp(self):
        self.session = self.client.session
        self.session['is_logged_in'] = False
        self.category_search = "Games"

    def test_add_item_response_code(self):
        """test that the addItem request returns the correct status code
        """
        url = reverse("addItem")
        response = self.client.get(url)

        self.assertTemplateUsed(response, 'addItem.html')
        self.assertEqual(response.status_code, 200)

        self.assertTemplateUsed(response, 'addItem.html')
        self.assertEqual(response.status_code, 200)

    def test_search_item_response_code(self):
        """test that the search item request returns the correct status code
        """
        url = reverse("searchItems")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
