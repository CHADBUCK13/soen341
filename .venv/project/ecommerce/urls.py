import imp
from unicodedata import name
from django.urls import path
from .views import home, signupBuyer, signupSeller
from .views import login
from .views import signup
from django.views.generic.base import TemplateView

urlpatterns = [
    path("", home, name="home"),
    path("login/", login, name="login"),
    path("signupOption/", signup, name="signupOption"),
    path("signupB/",signupBuyer,name="signupBuyer"),
    path("signupS/",signupSeller,name="signupSeller")
]
