from django import forms

class LoginForm(forms.Form):
    """
    Form that takes in an Email Address and a Password
    """
    email = forms.EmailField(
        label="Email",
        widget=forms.EmailInput(attrs={
            'class':'reg',
            'type':'email',
            'placeholder':'Email'
        }))

    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={
            'class':'reg',
            'type':'password',
            'placeholder':'Password'
        }))

    class Meta:
        fields=['email','password']