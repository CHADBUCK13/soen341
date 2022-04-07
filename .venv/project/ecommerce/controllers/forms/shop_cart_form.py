"""
This module contains all the forms required for the shopping cart
"""

from django import forms

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

