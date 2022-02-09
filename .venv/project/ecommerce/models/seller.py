from ..databaseContext import DatabaseContext

class Seller():
    def __init__(self,seller_signup_data=None,seller_data=None,email=None):
        """
        Creates a Seller
        """
        if seller_signup_data is not None:
            self.email=seller_signup_data['email']
            self.password=seller_signup_data['password1']
            self.name=seller_signup_data['name']
            self.country=seller_signup_data['country']
            self.city=seller_signup_data['city']
            self.address=seller_signup_data['address']
            self.postal_code=seller_signup_data['postal_code']
            self.service_number=seller_signup_data['service_number']
        
        if seller_data is not None:
            self.name=seller_data['name']
            self.country=seller_data['country']
            self.city=seller_data['city']
            self.address=seller_data['address']
            self.postal_code=seller_data['postal_code']
            self.service_number=seller_data['service_number']
        
        if email is not None:
            self.email=email
    
    def signup(self):
        """
        Signup the user by authenticating them and creating a document in the sellers table. 
        Returns: the auth info about the Seller
        """   
        # Creates the user
        return DatabaseContext().signup_as_seller(
            email=self.email,
            password=self.password,
            name=self.name,
            country=self.country,
            city=self.city,
            address=self.address,
            postal_code=self.postal_code,
            service_number=self.service_number
        )

    def accountType(self):
        return "seller"