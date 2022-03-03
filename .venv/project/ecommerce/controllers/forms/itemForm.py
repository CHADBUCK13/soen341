from django import forms
from ...api.itembrowsing import *

def categoryList():
    cat = get_categories()
    categoryList = []
    for c in cat:
        categoryList.append((c,c))
    return categoryList

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
        choices=categoryList()
        ))

    relatedCategories = forms.CharField(
        label="Related Item Categories",
        required=True,
        widget=forms.Select(attrs={
            'class':'itemForm',
            'type':'text',
            'placeholder':'Others'
        },
        choices=categoryList()
        ))

    amount = forms.IntegerField(
        label="Amount In Stock",
        required=True,
        min_value=0,
        widget=forms.NumberInput(attrs={
            'class':'itemForm',
            'type':'number',
            'placeholder':0
        })
    )

    image = forms.ImageField(
        label="Item Image",
        required=True,
        widget=forms.FileInput(attrs={
            'type':'file',
            'name':'image'
        }))
    
class Meta:
    fields=['name','price','description','weight','category','relatedCategories','amount','image']