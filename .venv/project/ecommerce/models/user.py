from ..api.accountContext import AccountContext
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
        return AccountContext().is_buyer(email)
    
    def is_seller(email):
        """
        Returns TRUE if User is a Seller.
        """
        return AccountContext().is_seller(email)

    def reset_password(email):
        """
        Sends a Password Reset Link to the given Email.
        """
        AccountContext().reset_password(email)


    def getUser(idToken):
        """
        Get the User linked to the idToken from the DB.
        """

        # Get the email for the account represented by the token
        email=AccountContext().get_account_info(idToken)['users'][0]['email']
        
        # If the email belongs to a buyer, then return the buyer
        if AccountContext().is_buyer(email):
            return Buyer(email=email,buyer_data=AccountContext().get_buyer(email))
        # Otherwise, return the seller
        else:
            return Seller(email=email,seller_data=AccountContext().get_seller(email))


    def login(login_data):
        """
        Login the user in the DB.
        """

        # Try to login as a buyer
        user = AccountContext().login_as_buyer(
            email=login_data['email'],
            password=login_data['password']
        )

        # If the login was successful, return the buyer info
        if user is not False:
            return user

        # If the user logging in is not a buyer, then try to login as a seller
        return AccountContext().login_as_seller(
            email=login_data['email'],
            password=login_data['password']
        )       