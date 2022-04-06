"""
This module contains all the forms required for the shopping cart
"""

from django import forms

# class couponForm(forms.Form):
#     code = forms.CharField(widget=forms.TextInput(attrs={
#         'class': 'form-control',
#         'placeholder': 'Promo code',
#         'aria-label': 'Recipient\'s username',
#         'aria-describedby': 'basic-addon2'
#     }))

class AddItemForm(forms.Form):
    """
    Form that holds an item as hidden input
    """
    item = forms.HiddenInput()

    class Meta:
        """
        Meta data for the add item form
        """
        fields=['item']

#Checkout form
##Payment/Refund form?
