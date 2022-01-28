import imp
from django.urls import path
from .views import home
from .views import login
from django.views.generic.base import TemplateView

urlpatterns = [
    path("", home, name="home"),
    path("login/", login, name="login")
]