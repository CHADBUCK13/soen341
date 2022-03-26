from ecommerce.api.account_context import signup_as_buyer

class Buyer():
    """
    User who buys items from other users.
    """

    def __init__(self,buyer_signup_data=None,buyer_data=None,email=None):
        """
        Create a new Buyer instance.
        """

        # Create the Buyer with the info from the signup form
        if buyer_signup_data is not None:
            self.email=buyer_signup_data['email']
            self.password=buyer_signup_data['password1']
            self.firstname=buyer_signup_data['firstname']
            self.lastname=buyer_signup_data['lastname']
            self.country=buyer_signup_data['country']
            self.city=buyer_signup_data['city']
            self.address=buyer_signup_data['address']
            self.postal_code=buyer_signup_data['postal_code']
            self.date_of_birth=buyer_signup_data['date_of_birth']
        
        # Create the Buyer with the info from the db
        if buyer_data is not None:
            self.firstname=buyer_data['firstname']
            self.lastname=buyer_data['lastname']
            self.country=buyer_data['country']
            self.city=buyer_data['city']
            self.address=buyer_data['address']
            self.postal_code=buyer_data['postal_code']
            self.date_of_birth=buyer_data['date_of_birth']
        
        # Set the Buyer's email if its given
        if email is not None:
            self.email=email
    
    def signup(self):
        """
        Signup the Buyer by authenticating him and creating a document in the buyers table. 
        Returns: the auth info about the Buyer
        """

        # Signup the buyer
        return signup_as_buyer(
            email=self.email,
            password=self.password,
            firstname=self.firstname,
            lastname=self.lastname,
            country=self.country,
            city=self.city,
            address=self.address,
            postal_code=self.postal_code,
            date_of_birth=self.date_of_birth
        )

    def accountType(self):
        """
        Returns: 'buyer'
        """
        return "buyer"



    

        
