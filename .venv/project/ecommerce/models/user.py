"""Contains user class only
"""
from ecommerce.api.account_context import get_account_info, get_buyer, get_seller, is_buyer,\
    is_seller, login_as_buyer, login_as_seller, reset_password
from .buyer import Buyer
from .seller import Seller


class User():
    """
    Buyer or Seller that is already signed up in the db.
    """

    def is_buyer(email):
        """
        Returns TRUE if User is a Buyer.
        """
        return is_buyer(email)

    def is_seller(email):
        """
        Returns TRUE if User is a Seller.
        """
        return is_seller(email)

    def reset_password(email):
        """
        Sends a Password Reset Link to the given Email.
        """
        reset_password(email)

    def get_user(id_token):
        """
        Get the User linked to the idToken from the DB.
        """

        # Get the email for the account represented by the token
        email = get_account_info(id_token)['users'][0]['email']

        # If the email belongs to a buyer, then return the buyer
        if is_buyer(email):
            return Buyer(email=email, buyer_data=get_buyer(email))
        # Otherwise, return the seller
        else:
            return Seller(email=email, seller_data=get_seller(email))

    def login(login_data):
        """
        Login the user in the DB.
        """

        # Try to login as a buyer
        user = login_as_buyer(
            email=login_data['email'],
            password=login_data['password']
        )

        # If the login was successful, return the buyer info
        if user is not False:
            return user

        # If the user logging in is not a buyer, then try to login as a seller
        return login_as_seller(
            email=login_data['email'],
            password=login_data['password']
        )
