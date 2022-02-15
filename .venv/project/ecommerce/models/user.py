from ..databaseContext import DatabaseContext
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
        return DatabaseContext().is_buyer(email)
    
    def is_seller(email):
        """
        Returns TRUE if User is a Seller.
        """
        return DatabaseContext().is_seller(email)

    def getUser(idToken):
        """
        Get the User linked to the idToken from the DB.
        """

        # Get the email for the account represented by the token
        email=DatabaseContext().get_account_info(idToken)['users'][0]['email']
        
        # If the email belongs to a buyer, then return the buyer
        if DatabaseContext().is_buyer(email):
            return Buyer(email=email,buyer_data=DatabaseContext().get_buyer(email))
        # Otherwise, return the seller
        else:
            return Seller(email=email,seller_data=DatabaseContext().get_seller(email))


    def login(login_data):
        """
        Login the user in the DB.
        """

        # Try to login as a buyer
        user = DatabaseContext().login_as_buyer(
            email=login_data['email'],
            password=login_data['password']
        )

        # If the login was successful, return the buyer info
        if user is not False:
            return user

        # If the user logging in is not a buyer, then try to login as a seller
        return DatabaseContext().login_as_seller(
            email=login_data['email'],
            password=login_data['password']
        )       