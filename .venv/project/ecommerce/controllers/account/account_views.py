"""
This module contains all the logic required the Account views
"""

from django.shortcuts import redirect, render
from ecommerce.api.account_context import show_error_message
from ecommerce.models.seller import Seller
from ecommerce.models.buyer import Buyer
from ecommerce.models.user import User
from ecommerce.controllers.forms.signup_form import BuyerSignupForm, SellerSignupForm
from ecommerce.controllers.forms.login_form import LoginForm
from ecommerce.controllers.forms.reset_password_form import ResetPasswordForm

def login(request, reset_msg=""):
    """
    Logins a user.
    """

    # Login form has been submitted
    if request.method == "POST":

        # Get login form info
        login_form = LoginForm(request.POST)

        # The form info is valid
        if login_form.is_valid():

            # Authenticate the user
            user = User.login(login_form.data)

            # User does not exist, ask him to create an account
            if user is False:
                login_form.add_error(None,
                "No Account exists for the given Email Address. Please go to the Signup Page.")

            # An error occured, so show an error message to the user
            if 'error' in user:
                login_form.add_error(None, show_error_message(user))

            else:

                if User.is_seller(user['email']):
                    request.session['is_seller']=True
                else:
                    request.session['is_seller']=False

                # Add the login status to the session
                request.session['is_logged_in']=True
                request.session.modified = True

                # Go back to the Home Page
                redirect_page = redirect('home')

                # Set the Id_token and the refresh_token as Cookies
                redirect_page.set_cookie('idToken', user['idToken'], max_age = 1800)
                redirect_page.set_cookie('refreshToken',user['refreshToken'],max_age=3600)

                # Go to home page
                return redirect_page
    # Not a POST Request
    else:
        # Create the Login Form
        login_form = LoginForm()

    # Show the login page with the login form
    return render(request,'register.html',{"loginForm":login_form,"reset_msg":reset_msg})


def reset_password(request):
    """
    Sends a reset password link by email.
    """

    if request.method == "POST":

        reset_form = ResetPasswordForm(request.POST)

        if reset_form.is_valid():

            email = reset_form.cleaned_data['email']

            if User.is_buyer(email) or User.is_seller(email):
                User.reset_password(email)
                return login(request, reset_msg="Password Reset Link has been Sent!")
            reset_form.add_error(None,"No Account Exists with the given Email.")
    else:
        reset_form = ResetPasswordForm()

    return render(request,'reset_password.html',{'reset_form':reset_form})


def logout(request):
    """
    Logouts the user that is currently logged in.
    """

    # Get both the id_token and the refresh_token
    id_token = request.COOKIES.get('idToken',None)
    refresh_token = request.COOKIES.get('refreshToken',None)

    # Save the login status to the session
    request.session['is_logged_in']=False
    request.session.modified = True

    # Go back to the Home Page
    redirect_page = redirect('home')

    # Delete the id_token if it exists
    if id_token is not None:
        redirect_page.delete_cookie('idToken')

    # Delete the refresh_token if it exists
    if refresh_token is not None:
        redirect_page.delete_cookie('refreshToken')

    # Go to home page
    return redirect_page

def signup_buyer(request):
    """
    Signup a new Buyer Account.
    """
    # Signup form is being submitted
    if request.method == "POST":

        # Get the Info from the form
        signup_form = BuyerSignupForm(request.POST)

        # Form input is Valid
        if signup_form.is_valid():

            # Signup the buyer in the DB.
            buyer_info = Buyer(buyer_signup_data=signup_form.data).signup()

            # If the DB returns an error, show it in the form
            if 'error' in buyer_info:
                signup_form.add_error(None,show_error_message(buyer_info))

            # Otherwise, login the user.
            else:
                # Add the login status to the session
                request.session['is_seller']=False
                request.session['is_logged_in']=True
                request.session.modified = True

                # Go back to the Home Page
                redirect_page = redirect('home')

                # Set the Id_token and the refresh_token as Cookies
                redirect_page.set_cookie('idToken', buyer_info['idToken'], max_age = 1800)
                redirect_page.set_cookie('refreshToken',buyer_info['refreshToken'],max_age=3600)

                # Go to home page
                return redirect_page
    # Buyer Signup Form is being accessed
    else:
        # Get the Buyer Signup Form
        signup_form = BuyerSignupForm()

    # Show the Signup Page with the Buyer Signup Form
    return render(request, 'signup.html',{"signupForm":signup_form})

def signup_seller(request):
    """
    Signup a new Seller Account.
    """
    # Signup form is being submitted
    if request.method == "POST":

        # Get the Info from the form
        signup_form = SellerSignupForm(request.POST)

        # Form input is Valid
        if signup_form.is_valid():

            # Signup the seller in the DB.
            seller_info = Seller(seller_signup_data=signup_form.data).signup()

            # If the DB returns an error, show it in the form
            if 'error' in seller_info:
                signup_form.add_error(None,show_error_message(seller_info))

            # Otherwise, login the user.
            else:
                # Add the login status to the session
                request.session['is_seller']=True
                request.session['is_logged_in']=True
                request.session.modified = True

                # Go back to the Home Page
                redirect_page = redirect('home')

                # Set the Id_token and the refresh_token as Cookies
                redirect_page.set_cookie('idToken', seller_info['idToken'], max_age = 1800)
                redirect_page.set_cookie('refreshToken',seller_info['refreshToken'],max_age=3600)

                # Go to home page
                return redirect_page
    # Seller Signup Form is being accessed    
    else:
        # Get the Seller Signup Form
        signup_form = SellerSignupForm()

    # Show the Signup Page with the Seller Signup Form
    return render(request, 'signup.html',{"signupForm":signup_form})
