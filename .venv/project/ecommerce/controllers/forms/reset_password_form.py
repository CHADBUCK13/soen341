"""
This module contains the form required to reset a password
"""

from django import forms

class ResetPasswordForm(forms.Form):
    """
    Form that takes in an Email Address
    """
    email = forms.EmailField(
        label="Email",
        widget=forms.EmailInput(attrs={
            'class':'reg',
            'type':'email',
            'placeholder':'Email'
        }))

    class Meta:
        """
        Meta data for the reset password form
        """
        fields=['email']
