"""
This module contains all the logic required seller and buyer banking forms
"""

from django import forms

class BankingBuyerForm(forms.Form):
    """
    Forms that allows a Buyer to enter his banking information.
    """

    firstname = forms.CharField(
        label="Cardholder First Name",
        required=True,
        widget=forms.TextInput(attrs={
            'class':'reg',
            'type':'text',
            'placeholder':'First Name'
        }))

    lastname = forms.CharField(
        label="Cardholder Last Name",
        required=True,
        widget=forms.TextInput(attrs={
            'class':'reg',
            'type':'text',
            'placeholder':'Last Name'
        }))

    number = forms.CharField(
        label="Card Number",
        min_length=16,
        max_length=16,
        required=True,
        widget=forms.NumberInput(attrs={
            'class':'reg',
            'type':'number',
            'placeholder':'#### #### #### ####'
        }))

    expirationDate = forms.CharField(
        label="Card Expiration Date",
        required=True,
        min_length=4,
        max_length=4,
        widget=forms.NumberInput(attrs={
            'class':'reg',
            'type':'number',
            'placeholder':'MMYY'
        }))
  
    cvv = forms.CharField(
        label="Card CVV",
        min_length=3,
        max_length=3,
        required=True,
        widget=forms.NumberInput(attrs={
            'class':'reg',
            'type':'number',
            'placeholder':'###'
        }))


    class Meta:
        """
        Banking Buyer Form MetaData
        """
        fields=['firstname','lastname','number','expirationDate','cvv']

class BankingSellerForm(forms.Form):
    """
    Forms that allows a Seller to enter his banking information.
    """

    transit = forms.CharField(
        label="Transit (Branch) Number",
        required=True,
        min_length=5,
        max_length=5,
        widget=forms.NumberInput(attrs={
            'class':'reg',
            'type':'number',
            'placeholder':'#####'
        }))

    institution = forms.CharField(
        label="Institution Number",
        required=True,
        min_length=3,
        max_length=3,
        widget=forms.TextInput(attrs={
            'class':'reg',
            'type':'number',
            'placeholder':'###'
        }))

    account = forms.CharField(
        label="Account Number",
        required=True,
        min_length=7,
        max_length=7,
        widget=forms.TextInput(attrs={
            'class':'reg',
            'type':'number',
            'placeholder':'#######'
        }))

    class Meta:
        """
        Banking Seller Form MetaData
        """
        fields=['transit','institution','account']