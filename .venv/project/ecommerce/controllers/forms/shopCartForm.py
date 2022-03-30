
from django import forms
# class couponForm(forms.Form):
#     code = forms.CharField(widget=forms.TextInput(attrs={
#         'class': 'form-control',
#         'placeholder': 'Promo code',
#         'aria-label': 'Recipient\'s username',
#         'aria-describedby': 'basic-addon2'
#     }))


class AddItemForm(forms.Form):
    item = forms.HiddenInput()

    class Meta:
        fields = ['item']

# Checkout form
# Payment/Refund form?
