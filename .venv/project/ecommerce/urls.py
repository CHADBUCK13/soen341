import imp
from unicodedata import name
from django.urls import path
from .views import home
from .views import login
from .views import signup
from django.views.generic.base import TemplateView

urlpatterns = [
    path("", home, name="home"),
    path("login/", login, name="login"),
    path("signup/", signup, name="signup")
]
