"""
This contains tests for login, signup, logout and home views and item browsing
"""
from django.test import TestCase
from django.urls import reverse


class TestLogin(TestCase):
    """
    tests for the login view
    """

    def test_login_page_response_code(self):
        """
        tests if the login request returns the correct response
        """
        url = reverse("login")
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'register.html')


class TestSignup(TestCase):
    """
    tests for the login view
    """

    def test_signup_buyer_page_response_code(self):
        """Test the signup buyer request returns the correct response code
        """
        url = reverse("signupBuyer")
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'signup.html')

    def test_signup_seller_page_response_code(self):
        """_summary_
        """
        url = reverse("signupSeller")
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'signup.html')
        self.assertEqual(response.status_code, 200)


class TestLogout(TestCase):
    """Test the logout view functions
    """

    def test_logout_response_code(self):
        """Test the logout request returns the correct response code
        """
        url = reverse("logout")
        response = self.client.get(url)

        self.assertEqual(response.status_code, 302)


class Testhome(TestCase):
    """Test the home view functions
    """

    def setUp(self):
        self.session = self.client.session
        self.session['is_logged_in'] = False
        self.category_search = "Games"

    def test_home_response_code(self):
        """test the home request returns the correct response code
        """
        url = reverse("home")
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'home.html')
        self.assertEqual(response.status_code, 200)

    def test_logged_in_response(self):
        """test if the logged in response returns the expected results
        """
        self.assertFalse( self.session['is_logged_in'])
        
        
class Testitem_browsingViews(TestCase):
   """test the functions in itembrowsing views
    """

    def setUp(self):
        self.session = self.client.session
        self.session['is_logged_in'] = False
        self.category_search = "Games"

    def test_add_item_response_code(self):
        """test if the add item request returns the correct response
        """
        url = reverse("addItem")
        response = self.client.get(url)

        self.assertTemplateUsed(response, 'addItem.html')
        self.assertEqual(response.status_code, 200)
    def test_search_item_response_code(self):
        """test that the serach item request returns the correct response code
        """
        url = reverse("searchItems")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
