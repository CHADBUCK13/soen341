from ..databaseContext import DatabaseContext
from .buyer import Buyer
from .seller import Seller

class User():

    def is_buyer(email):
        return DatabaseContext().is_buyer(email)
    
    def is_seller(email):
        return DatabaseContext().is_seller(email)

    def getUser(idToken):
        email=DatabaseContext().get_account_info(idToken)['users'][0]['email']
        if DatabaseContext().is_buyer(email):
            return Buyer(email=email,buyer_data=DatabaseContext().get_buyer(email))
        else:
            return Seller(email=email,seller_data=DatabaseContext().get_seller(email))


    def login(login_data):
        user = DatabaseContext().login_as_buyer(
            email=login_data['email'],
            password=login_data['password']
        )
        if user is not False:
            return user

        user = DatabaseContext().login_as_seller(
            email=login_data['email'],
            password=login_data['password']
        )       

        return user




