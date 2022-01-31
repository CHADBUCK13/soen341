import uuid
from django.http import HttpResponse
from django.shortcuts import render,redirect

# Account Creation/Login Forms Imports
from .controllers.SignupForm import BuyerSignupForm 

# Firestore Imports
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from firebase_admin import auth



def home(request):
    return render(request,'home.html')
    #return HttpResponse("Hello, SOEN 341 Group!")

def login(request):
    return render(request, 'login.html')

def signup(request):
    # TODO: Passwords should be hashed!!!

    if request.method == "POST":
        signup_form = BuyerSignupForm(request.POST)
        if signup_form.is_valid():

            # User Auth
            user = auth.create_user(
                uid=signup_form.data['email'],
                email=signup_form.data['email'],
                email_verified=True,
                password=signup_form.data['password1'],
                display_name=str(signup_form.data['firstname']+" "+signup_form.data['lastname']),
                disabled=False,
            )

            # DB Access
            #db= firestore.client()
            #db.collection('accounts').add({'username':signup_form.data['username'],'email':'email@gmail.com','password':signup_form.data['password1']})
            return redirect(home)
    else:
        signup_form = BuyerSignupForm()
    
    return render(request, 'signup.html', {"form":signup_form})