from attr import attr
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class BuyerSignupForm(UserCreationForm):
    """
    Form that takes in the required fields to Signup a Buyer.
    """
    
    email = forms.EmailField(
        label="Email", 
        widget=forms.EmailInput(attrs={
            'class':'reg',
            'type':'email',
            'placeholder':'Email'
        }))

    firstname = forms.CharField(
        label="First Name",
        widget=forms.TextInput(attrs={
            'class':'reg',
            'type':'text',
            'placeholder':'First Name'
        }))
    lastname = forms.CharField(
        label="Last Name",
        widget=forms.TextInput(attrs={
            'class':'reg',
            'type':'text',
            'placeholder':'Last Name'
        }))
    
    country = forms.CharField(
        label="Country",
        widget=forms.TextInput(attrs={
            'class':'reg',
            'type':'text',
            'placeholder':'Country'
        }))

    city = forms.CharField(
        label="City",
        widget=forms.TextInput(attrs={
            'class':'reg',
            'type':'text',
            'placeholder':'City'
        }))
    
    address = forms.CharField(
        label="Address",
        widget=forms.TextInput(attrs={
            'class':'reg',
            'type':'text',
            'placeholder':'Address'
        }))

    postal_code = forms.CharField(
        label="Postal Code",
        widget=forms.TextInput(attrs={
            'class':'reg',
            'type':'text',
            'placeholder':'Postal Code'
        }))

    date_of_birth = forms.CharField(
        label="Date of Birth",
        widget=forms.TextInput(attrs={
            'class':'reg',
            'type':'text',
            'placeholder':'Date of Birth'
        }))
    

    class Meta:
        model=User
        fields=["email","password1","password2","firstname","lastname","country","city","address","postal_code","date_of_birth"]

class SellerSignupForm(UserCreationForm):
    """
    Form that takes in the required fields to Signup a Seller.
    """

    email = forms.EmailField(
        label="Email", 
        widget=forms.EmailInput(attrs={
            'class':'reg',
            'type':'email',
            'placeholder':'Email'
        }))
    name = forms.CharField(
        label='Name',
        widget=forms.TextInput(attrs={
            'class':'reg',
            'type':'text',
            'placeholder':'Name'
        }))
    country = forms.CharField(
        label="Country",
        widget=forms.TextInput(attrs={
            'class':'reg',
            'type':'text',
            'placeholder':'Country'
        }))

    city = forms.CharField(
        label="City",
        widget=forms.TextInput(attrs={
            'class':'reg',
            'type':'text',
            'placeholder':'City'
        }))
    address = forms.CharField(
        label="Address",
        widget=forms.TextInput(attrs={
            'class':'reg',
            'type':'text',
            'placeholder':'Address'
        }))

    postal_code = forms.CharField(
        label="Postal Code",
        widget=forms.TextInput(attrs={
            'class':'reg',
            'type':'text',
            'placeholder':'Postal Code'
        }))
    service_number=forms.CharField(
        label='Service Number',
        widget=forms.TextInput(attrs={
            'class':'reg',
            'type':'text',
            'placeholder':'Service Number' 
        }))

    class Meta:
        model=User
        fields=["email","password1","password2","name","country","city","address","postal_code","service_number"]