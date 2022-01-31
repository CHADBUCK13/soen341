from dataclasses import field
import email
import imp
from tkinter.tix import Form
from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class BuyerSignupForm(UserCreationForm):
    email = forms.EmailField()
    firstname = forms.CharField()
    lastname = forms.CharField()
    country = forms.CharField()
    city= forms.CharField()
    address = forms.CharField()
    postal_code=forms.CharField()
    date_of_birth=forms.CharField()
    password=forms.PasswordInput()




    class Meta:
        model=User
        fields=["email","firstname","lastname","country","city","address","password1","password2","postal_code","date_of_birth"]