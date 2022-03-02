
import os
from time import sleep
from django.test import TestCase
from django.urls import reverse
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

SELENIUM_GRID_HOST = os.environ.get('SELENIUM_GRID_HOST', 'localhost')

# REDO WITHOUT GUI TESTING

#class TestLogin(TestCase):    
    # def setUp(self):
    #     self.driver = webdriver.Remote(
    #         desired_capabilities=DesiredCapabilities.CHROME,
    #         command_executor="http://%s:4444" % SELENIUM_GRID_HOST
    #     )

    # def test_login_page_response_code(self):
    #     url = reverse("login")
    #     response = self.client.get(url)
        
    #     self.assertEqual(response.status_code, 200)

    # def test_login_fail(self):
    #     self.driver.get("http://localhost:8000/login/")
    #     self.driver.find_element_by_id('id_email').send_keys("tessst@gmail.com")
    #     self.driver.find_element_by_id('id_password').send_keys("Djjango1234")
    #     el = self.driver.find_element_by_id("login_form")
    #     el.submit()
    #     self.assertNotIn("http://localhost:8000/home/", self.driver.current_url)

    # def tearDown(self):
    #     self.driver.quit



class TestSignup(TestCase):
    
    def test_signup_option_page_response_code(self):
        url = reverse("signupOption")
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, 200)
    
    def test_signup_buyer_page_response_code(self):
        url = reverse("signupBuyer")
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, 200)
    
    def test_signup_seller_page_response_code(self):
        url = reverse("signupSeller")
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, 200)

class TestLogout(TestCase):

    def test_logout_response_code(self):
        url = reverse("logout")
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, 302)