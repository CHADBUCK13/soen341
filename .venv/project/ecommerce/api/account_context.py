"""
This contains all logic to use firebase accounts
"""

from datetime import datetime
import json
from requests.exceptions import HTTPError
import pyrebase
from firebase_admin import firestore


FIREBASE_CONFIG = json.load(open("pyrebaseConfig.json", encoding="utf-8"))


firebase = pyrebase.initialize_app(FIREBASE_CONFIG)
auth = firebase.auth()
# firebase_admin.initialize_app()
db = firestore.client()


def signup_as_buyer(
    email,
    password,
    firstname="",
    lastname="",
    country="",
    city="",
    address="",
    postal_code="",
    date_of_birth="",
):
    """
    This function takes buyer info and adds the user to the database
    """
    try:
        # Set User Type
        account_location = "buyers"

        # Create New User
        user = auth.create_user_with_email_and_password(email, password)

        # Verify Email Address
        auth.send_email_verification(user["idToken"])

        buyer_data = {
            "firstname": firstname,
            "lastname": lastname,
            "country": country,
            "city": city,
            "address": address,
            "postal_code": postal_code,
            "date_of_birth": date_of_birth,
        }

        # Add User in its Appropriate Account Table
        db.collection(account_location).document(user["email"]).set(buyer_data)

        # Return the New User
        return user

    except HTTPError as error:
        return json.loads(error.strerror)


def signup_as_seller(
    email,
    password,
    name="",
    country="",
    city="",
    address="",
    postal_code="",
    service_number="",
    logo="",
):
    """
    This function takes seller info and adds the user to the database
    """
    try:
        # Set User Type
        account_location = "sellers"

        # Create New User
        user = auth.create_user_with_email_and_password(email, password)

        # Verify Email Address
        auth.send_email_verification(user["idToken"])

        seller_data = {
            "name": name,
            "country": country,
            "city": city,
            "address": address,
            "postal_code": postal_code,
            "signup_date": datetime.now().strftime("%Y/%m/%d"),
            "service_number": service_number,
            "logo": logo,
        }

        # Add User in its Appropriate Account Table
        db.collection(account_location).document(user["email"]).set(seller_data)

        # Return the New User
        return user

    except HTTPError as error:
        print(error)


def login_as_buyer(email, password):
    """
    This function takes buyer login info and validates user
    """
    try:
        # Validate Status as Buyer
        if db.collection("buyers").document(email).get().exists:

            # Sign In the User
            user = auth.sign_in_with_email_and_password(email, password)

            return user
        else:
            return False
    except HTTPError as error:
        return json.loads(error.strerror)


def login_as_seller(email, password):
    """
    This function takes seller login info and validates user
    """
    try:
        # Validate Status as Seller
        if db.collection("sellers").document(email).get().exists:

            # Sign In the User
            user = auth.sign_in_with_email_and_password(email, password)

            return user
        else:
            return False
    except HTTPError as error:
        return json.loads(error.strerror)


def get_account_info(id_token):
    """
    This function takes user id_token and returns firebase info on the account
    """
    try:
        user = auth.get_account_info(id_token)
        return user
    except HTTPError as error:
        return json.loads(error.strerror)


def get_account_from_refresh_token(refresh_token):
    """
    This function takes user login info and returns user account
    """
    try:
        user = auth.get_account_info(auth.refresh(refresh_token)["idToken"])
        return user
    except HTTPError as error:
        return json.loads(error.strerror)


def refresh_id_token(request, redirect):
    """
    Refreshes firebase idToken
    """
    try:
        id_token = request.COOKIES.get("idToken", None)
        refresh_token = request.COOKIES.get("refreshToken", None)

        if id_token is None and refresh_token is not None:
            user = auth.refresh(refresh_token)
            redirect.set_cookie("idToken", user["idToken"], max_age=1800)
            redirect.set_cookie("refreshToken", user["refreshToken"], max_age=3600)
            return redirect
        elif id_token is None and refresh_token is None:
            return False
        else:
            return request
    except HTTPError as error:
        return json.loads(error.strerror)


def is_buyer(email):
    """
    Checks if user is a buyer type account
    """
    try:
        return db.collection("buyers").document(email).get().exists
    except HTTPError as error:
        return json.loads(error.strerror)


def is_seller(email):
    """
    Checks if user is a seller type account
    """
    try:
        return db.collection("sellers").document(email).get().exists
    except HTTPError as error:
        return json.loads(error.strerror)


def get_buyer(email):
    """
    Takes email and return firebase account matching
    """
    try:
        return db.collection("buyers").document(email).get().to_dict()
    except HTTPError as error:
        return json.loads(error.strerror)


def get_seller(email):
    """
    Takes email and return firebase account matching
    """
    try:
        return db.collection("sellers").document(email).get().to_dict()
    except HTTPError as error:
        return json.loads(error.strerror)


def reset_password(email):
    """
    Takes email and resets firebase account password
    """
    auth.send_password_reset_email(email)


def show_error_message(error):
    """
    Function to show error message
    """
    if error["error"]["message"] == "EMAIL_EXISTS":
        return "This Email Address is already used by another Account."
    if error["error"]["message"] == "INVALID_PASSWORD":
        return (
            "Login Failed. An incorrect Email Address and/or Password has been given."
        )
    if error["error"]["message"] == (
        "TOO_MANY_ATTEMPTS_TRY_LATER : Access to this account has been temporarily disabled"
        "due to many failed login attempts. You can immediately"
        " restore it by resetting your password or you can try again later."
    ):
        return (
            "Access to this account has been temporarily disabled"
            "due to many failed login attempts. You can try again later."
        )
    else:
        return error["error"]["message"]
