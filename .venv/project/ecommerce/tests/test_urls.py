from django.test import TestCase
from django.urls import reverse, resolve
from ..views import home
from ..controllers.itemBrowsing.itemBrowsingViews import addItem,searchItems
from ..controllers.account.accountViews import login,logout,signupBuyer,signupSeller


class TestUrls(TestCase):
    def test_home_url_is_resolved(self):
        url = reverse("home")
        self.assertEqual(resolve(url).func, home)
        

    def test_login_url_is_resolved(self):
        url = reverse("login")
        self.assertEqual(resolve(url).func, login)
        
        
    def test_logout_url_is_resolved(self):
        url = reverse("logout")
        self.assertEqual(resolve(url).func, logout)
    
    
    def test_signupBuyer_url_is_resolved(self):
        url = reverse("signupBuyer")
        self.assertEqual(resolve(url).func, signupBuyer)
        
        
    def test_signupSeller_url_is_resolved(self):
        url = reverse("signupSeller")
        self.assertEqual(resolve(url).func, signupSeller)
        
    def test_addItem_url_is_resolved(self):
        url = reverse("addItem")
        self.assertEqual(resolve(url).func, addItem)
        
    def test_searchItems_url_is_resolved(self):
        url = reverse("searchItems")
        self.assertEqual(resolve(url).func, searchItems)