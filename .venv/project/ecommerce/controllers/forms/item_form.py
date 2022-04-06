"""
This module contains all the logic required for adding item with a form
"""

from django import forms
from ecommerce.api.item_browsing import get_categories

def category_list():
    """
    Gets a list of all possible categories
    """
    categories = get_categories()
    categories_list = []
    for category in categories:
        categories_list.append((category,category))
    return categories_list

class ItemForm(forms.Form):
    """
    Form that Allows an Item to be put on sale
    """

    name = forms.CharField(
        label="Item Name",
        required=True,
        widget=forms.TextInput(attrs={
            'class':'itemForm',
            'type':'text',
            'placeholder':'Item Name'
        }))

    price = forms.DecimalField(
        label="Item Price (CAD)",
        min_value=0,
        required=True,
        widget=forms.NumberInput(attrs={
            'class':'itemForm',
            'type':'number',
            'placeholder':0
        }))

    description = forms.CharField(
        label="Item Description",
        required=True,
        widget=forms.TextInput(attrs={
            'class':'itemForm',
            'type':'text',
            'placeholder':'Description'
        }))

    weight = forms.DecimalField(
        label="Item Weight (kg)",
        min_value=0,
        required=True,
        widget=forms.NumberInput(attrs={
            'class':'itemForm',
            'type':'number',
            'placeholder':0
        }))

    category = forms.CharField(
        label="Item Category",
        required=True,
        widget=forms.Select(attrs={
            'class':'itemForm',
            'type':'text',
            'placeholder':'Others'
        },
        choices=category_list()
        ))

    relatedCategories = forms.CharField(
        label="Related Item Categories",
        required=True,
        widget=forms.Select(attrs={
            'class':'itemForm',
            'type':'text',
            'placeholder':'Others'
        },
        choices=category_list()
        ))

    image = forms.ImageField(
        label="Item Image",
        required=True,
        widget=forms.FileInput(attrs={
            'type':'file',
            'name':'image'
        }))

    class Meta:
        """
        Item form MetaData
        """
        fields=['name','price','description','weight','category','relatedCategories','image']
