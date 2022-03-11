
import os
from time import sleep
from django.test import TestCase
from django.urls import reverse
from ..api import itembrowsing
from ..views import home

class TestLogin(TestCase):    

    def test_login_page_response_code(self):
        url = reverse("login")
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response,'register.html')




class TestSignup(TestCase):
    
    def test_signup_buyer_page_response_code(self):
        url = reverse("signupBuyer")
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response,'signup.html')
    
    def test_signup_seller_page_response_code(self):
        url = reverse("signupSeller")
        response = self.client.get(url)
        self.assertTemplateUsed(response,'signup.html')
        self.assertEqual(response.status_code, 200)

class TestLogout(TestCase):

    def test_logout_response_code(self):
        url = reverse("logout")
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, 302)
        
        
class Testhome(TestCase):
    def test_home_response_code(self):
        url = reverse("home")
        response = self.client.get(url)
        self.assertTemplateUsed(response,'home.html')
        self.assertEqual(response.status_code, 200)
    