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
        fields=['email']