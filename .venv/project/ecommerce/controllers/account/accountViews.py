from django.shortcuts import redirect, render
from ...models.seller import Seller
from ...databaseContext import Errors
from ...models.buyer import Buyer
from ...models.user import User
from ...controllers.forms.signupForm import BuyerSignupForm, SellerSignupForm
from ...controllers.forms.loginForm import LoginForm


def login(request):
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
                login_form.add_error(None,"No Account exists for the given Email Address. Please go to the Signup Page.")
            
            # An error occured, so show an error message to the user
            if 'error' in user:
                login_form.add_error(None,Errors.ShowErrorMessage(user))
            
            else:
                # Add the login status to the session
                request.session['is_logged_in']=True
                request.session.modified = True

                # Go back to the Home Page
                redirectPage = redirect('home')

                # Set the IdToken and the refreshToken as Cookies
                redirectPage.set_cookie('idToken', user['idToken'], max_age = 1800)
                redirectPage.set_cookie('refreshToken',user['refreshToken'],max_age=3600)

                # Go to home page
                return redirectPage
    # Not a POST Request
    else:
        # Create the Login Form
        login_form = LoginForm()
    
    # Show the login page with the login form
    return render(request, 'login.html',{"form":login_form})

def logout(request):
    """
    Logouts the user that is currently logged in.
    """

    # Get both the idToken and the refreshToken
    idToken = request.COOKIES.get('idToken',None)
    refreshToken = request.COOKIES.get('refreshToken',None)

    # Save the login status to the session
    request.session['is_logged_in']=False
    request.session.modified = True

    # Go back to the Home Page
    redirectPage = redirect('home')

    # Delete the idToken if it exists
    if idToken is not None:
        redirectPage.delete_cookie('idToken')

    # Delete the refreshToken if it exists
    if refreshToken is not None:
        redirectPage.delete_cookie('refreshToken')

    # Go to home page
    return redirectPage

def signup(request):
    """
    Choose between Signing Up as a Buyer or as a Seller.
    """
    return render(request,'accountOption.html')

def signupBuyer(request):
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
            buyerInfo = Buyer(buyer_signup_data=signup_form.data).signup()

            # If the DB returns an error, show it in the form
            if 'error' in buyerInfo:
                signup_form.add_error(None,Errors.ShowErrorMessage(buyerInfo))

            # Otherwise, login the user.
            else:
                # Add the login status to the session
                request.session['is_logged_in']=True
                request.session.modified = True

                # Go back to the Home Page
                redirectPage = redirect('home')

                # Set the IdToken and the refreshToken as Cookies
                redirectPage.set_cookie('idToken', buyerInfo['idToken'], max_age = 1800)
                redirectPage.set_cookie('refreshToken',buyerInfo['refreshToken'],max_age=3600)

                # Go to home page
                return redirectPage
    # Buyer Signup Form is being accessed            
    else:
        # Get the Buyer Signup Form
        signup_form = BuyerSignupForm()

    # Show the Signup Page with the Buyer Signup Form
    return render(request, 'signup.html',{"form":signup_form})

def signupSeller(request):
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
            sellerInfo = Seller(seller_signup_data=signup_form.data).signup()

            # If the DB returns an error, show it in the form
            if 'error' in sellerInfo:
                signup_form.add_error(None,Errors.ShowErrorMessage(sellerInfo))

            # Otherwise, login the user.
            else:
                # Add the login status to the session
                request.session['is_logged_in']=True
                request.session.modified = True

                # Go back to the Home Page
                redirectPage = redirect('home')

                # Set the IdToken and the refreshToken as Cookies
                redirectPage.set_cookie('idToken', sellerInfo['idToken'], max_age = 1800)
                redirectPage.set_cookie('refreshToken',sellerInfo['refreshToken'],max_age=3600)

                # Go to home page
                return redirectPage
    # Seller Signup Form is being accessed            
    else:
        # Get the Seller Signup Form
        signup_form = SellerSignupForm()

    # Show the Signup Page with the Seller Signup Form
    return render(request, 'signup.html',{"form":signup_form})