from ast import For
from cProfile import label
from dataclasses import fields
import email
from fileinput import FileInput
from pyexpat import model
from this import d
from tkinter import Label
from tkinter.tix import Form
from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.admin import widgets

class LoginForm(forms.Form):
    email = forms.EmailField(label='Email',widget=forms.EmailInput())
    password = forms.CharField(label='Password', widget=forms.PasswordInput())

    class Meta:
        fields=['email','password']