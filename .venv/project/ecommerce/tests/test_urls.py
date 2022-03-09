import os
from time import sleep
from django.test import SimpleTestCase
from django.urls import reverse,resolve
from ..views import home


class TestUrls(SimpleTestCase):
    

    def home_url_is_resolved(self):
        url = reverse("home")
        print(resolve(url))
        self.assertEquals( resolve(url).func.view_class, home)
        