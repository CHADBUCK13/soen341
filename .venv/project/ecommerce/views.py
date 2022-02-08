import json
import re
from datetime import date
import uuid
from django.http import HttpResponse
from django.shortcuts import render,redirect

from .databaseContext import DatabaseContext

# Account Creation/Login Forms Imports
from .controllers.forms.signupForm import BuyerSignupForm, SellerSignupForm
from .controllers.forms.loginForm import LoginForm

# Firestore Imports
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from firebase_admin import auth


def home(request):
    return render(request,'home.html')
    #return HttpResponse("Hello, SOEN 341 Group!")

def login(request):
    if request.method == "POST":
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            db=DatabaseContext(json.load(open('../firebaseConfig.json')))
            user = db.login_as_seller(
                email=login_form.data['email'],
                password=login_form.data['password']
            )
            if 'error' in user:
                login_form.add_error(None,user['error']['message'])
            else:
                html = HttpResponse(render(request, 'home.html'))
                html.set_cookie('idToken', user['idToken'], max_age = 36000)
                return html
    else:
        login_form = LoginForm()
    return render(request, 'login.html',{"form":login_form})

def signup(request):
    return render(request,'accountOption.html')

def signupBuyer(request):
    if request.method == "POST":
        signup_form = BuyerSignupForm(request.POST)
        if signup_form.is_valid():
            
            db=DatabaseContext(json.load(open('../firebaseConfig.json')))
            user=db.signup_as_buyer(signup_form.data['email'],
            signup_form.data['password1'],
            signup_form.data['firstname'],
            signup_form.data['lastname'],
            signup_form.data['country'],
            signup_form.data['city'],
            signup_form.data['address'],
            signup_form.data['postal_code'],
            signup_form.data['date_of_birth'])
            return render(request,'home.html')
    else:
        signup_form = BuyerSignupForm()
    return render(request, 'signup.html',{"form":signup_form})

def signupSeller(request):
    if request.method == "POST":
        signup_form = SellerSignupForm(request.POST)
        if signup_form.is_valid():
            db=DatabaseContext(json.load(open('../firebaseConfig.json')))
            user=db.signup_as_seller(
            email=signup_form.data['email'],
            password=signup_form.data['password1'],
            name=signup_form.data['name'],
            country=signup_form.data['country'],
            city=signup_form.data['city'],
            address=signup_form.data['address'],
            postal_code=signup_form.data['postal_code'],
            service_number=signup_form.data['service_number'])
            return render(request,'home.html')
    else:
        signup_form = SellerSignupForm()
    return render(request, 'signup.html',{"form":signup_form})