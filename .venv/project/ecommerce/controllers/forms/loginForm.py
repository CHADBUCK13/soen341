from django import forms

class LoginForm(forms.Form):
    """
    Form that takes in an Email Address and a Password
    """
    email = forms.EmailField(label='Email',widget=forms.EmailInput())
    password = forms.CharField(label='Password', widget=forms.PasswordInput())

    class Meta:
        fields=['email','password']