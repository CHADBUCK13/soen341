from datetime import datetime
import json
from pickle import NONE
from requests.exceptions import HTTPError
import pyrebase
from firebase_admin import firestore


FIREBASE_CONFIG = json.load(open('pyrebaseConfig.json'))

class DatabaseContext():

    def __init__(self):
        self.firebase = pyrebase.initialize_app(FIREBASE_CONFIG)
        self.auth = self.firebase.auth()
        #firebase_admin.initialize_app()
        self.db = firestore.client()
        

    def signup_as_buyer(self,email,password,firstname="",lastname="",country="",city="",address="",postal_code="",date_of_birth=""):
        try:
            # Set User Type
            account_location="buyers"

            # Create New User
            user=self.auth.create_user_with_email_and_password(email,password)

            # Verify Email Address
            self.auth.send_email_verification(user['idToken'])

            buyer_data = {
                'firstname':firstname,
                'lastname':lastname,
                'country':country,
                'city':city,
                'address':address,
                'postal_code':postal_code,
                'date_of_birth':date_of_birth
            }

            # Add User in its Appropriate Account Table
            self.db.collection(account_location).document(user['email']).set(buyer_data)

            # Return the New User
            return user

        except HTTPError as e:
            return json.loads(e.strerror)

    def signup_as_seller(self,email,password,name="",country="",city="",address="",postal_code="",service_number="",logo=""):
        try:
            # Set User Type
            account_location="sellers"

            # Create New User
            user=self.auth.create_user_with_email_and_password(email,password)

            # Verify Email Address
            self.auth.send_email_verification(user['idToken'])

            seller_data = {
                'name':name,
                'country':country,
                'city':city,
                'address':address,
                'postal_code':postal_code,
                'signup_date':datetime.now().strftime("%Y/%m/%d"),
                'service_number':service_number,
                'logo':logo
            }

            # Add User in its Appropriate Account Table
            self.db.collection(account_location).document(user['email']).set(seller_data)

            # Return the New User
            return user

        except HTTPError as e:
            print(e)

    def login_as_buyer(self,email,password):
        try:
            # Validate Status as Buyer
            if self.db.collection('buyers').document(email).get().exists:
        
                # Sign In the User
                user = self.auth.sign_in_with_email_and_password(email,password)
        
                return user
            else: 
                return False
        except HTTPError as e:
            return json.loads(e.strerror)

    def login_as_seller(self,email,password):
        try:
            # Validate Status as Seller
            if self.db.collection('sellers').document(email).get().exists:
        
                # Sign In the User
                user = self.auth.sign_in_with_email_and_password(email,password)
        
                return user
            else: 
                return False
        except HTTPError as e:
            return json.loads(e.strerror)

    def get_account_info(self,idToken):
        try:
            user = self.auth.get_account_info(idToken)
            return user
        except HTTPError as e:
            return json.loads(e.strerror)

    def get_account_from_refreshToken(self,refreshToken):
        try:
            user = self.auth.get_account_info(self.auth.refresh(refreshToken)['idToken'])
            return user
        except HTTPError as e:
            return json.loads(e.strerror)

    def refresh_idToken(self,request, redirect):
        try:
            idToken = request.COOKIES.get('idToken',None)
            refreshToken = request.COOKIES.get('refreshToken',None)

            if idToken is None and refreshToken is not None:
                user = self.auth.refresh(refreshToken)
                redirect.set_cookie('idToken', user['idToken'], max_age = 1800)
                redirect.set_cookie('refreshToken',user['refreshToken'],max_age=3600)
                return redirect
            elif idToken is None and refreshToken is None:
                return False
            else:
                return request
        except HTTPError as e:
            return json.loads(e.strerror)

    def is_buyer(self,email):
        try:
            return self.db.collection('buyers').document(email).get().exists
        except HTTPError as e:
            return json.loads(e.strerror)


    def is_seller(self,email):
        try:
            return self.db.collection('sellers').document(email).get().exists
        except HTTPError as e:
            return json.loads(e.strerror)

    def get_buyer(self,email):
        try:
            return self.db.collection('buyers').document(email).get().to_dict()
        except HTTPError as e:
            return json.loads(e.strerror)

    def get_seller(self,email):
        try:
            return self.db.collection('sellers').document(email).get().to_dict()
        except HTTPError as e:
            return json.loads(e.strerror)

    def reset_password(self, email):
        """
        Sends a Password Reset link to the given Email.
        """
        self.auth.send_password_reset_email(email) 
   
    def delete_buyer(self, email, password):
            try:
            # Validate Status as Buyer
                if self.db.collection('buyers').document(email).get().exists:
        
                # Sign In the User
                    user = self.auth.sign_in_with_email_and_password(email, password)
                # delete the buyer    
                    self.auth.delete_user_account(user['idToken'])
                    self.db.collection('buyers').document(email).delete()
        
                
                else: 
                    return False
            except HTTPError as e:
                return json.loads(e.strerror)
        
    #Delete account func 
  #  def delete_account():
  #      details={
   #     'idToken':idToken
   # }
   #     r=requests.post('https://identitytoolkit.googleapis.com/v1/accounts:delete?key={}'.format(apikey),data=details)
    #    if 'error' in r.json().keys():
   #        return {'status':'error','message':r.json()['error']['message']}   
    #   return {'status':'success','data':r.json()}


class Errors():
    def ShowErrorMessage(error):
        if error['error']['message'] == "EMAIL_EXISTS":
            return "This Email Address is already used by another Account."
        if error['error']['message'] == "INVALID_PASSWORD":
            return "Login Failed. An incorrect Email Address and/or Password has been given."
        if error['error']['message']=="TOO_MANY_ATTEMPTS_TRY_LATER : Access to this account has been temporarily disabled due to many failed login attempts. You can immediately restore it by resetting your password or you can try again later.":
            return "Access to this account has been temporarily disabled due to many failed login attempts. You can try again later."
        else:
            return error['error']['message']
        