from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class BuyerSignupForm(UserCreationForm):
    """
    Form that takes in the required fields to Signup a Buyer.
    """
    
    email = forms.EmailField(label='Email', widget=forms.EmailInput())
    firstname = forms.CharField(label='First Name')
    lastname = forms.CharField(label='Last Name')
    country = forms.CharField(label='Country')
    city= forms.CharField(label='City')
    address = forms.CharField(label='Address')
    postal_code=forms.CharField(label='Postal Code')
    date_of_birth=forms.CharField(label='Date of Birth')

    class Meta:
        model=User
        fields=["email","password1","password2","firstname","lastname","country","city","address","postal_code","date_of_birth"]

class SellerSignupForm(UserCreationForm):
    """
    Form that takes in the required fields to Signup a Seller.
    """

    email = forms.EmailField(label='Email', widget=forms.EmailInput())
    name = forms.CharField(label='Name')
    country = forms.CharField(label='Country')
    city= forms.CharField(label='City')
    address = forms.CharField(label='Address')
    postal_code=forms.CharField(label='Postal Code')
    service_number=forms.CharField(label='Service Number')

    class Meta:
        model=User
        fields=["email","password1","password2","name","country","city","address","postal_code","service_number"]