from datetime import date, datetime
from email import message
import json
from logging import exception
from msilib.schema import File
import re
from unittest import result
from httplib2 import Http
from requests.exceptions import HTTPError
import pyrebase
from firebase_admin import firestore
import firebase_admin

class DatabaseContext():

    def __init__(self,config):
        self.firebase = pyrebase.initialize_app(config)
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
            #auth.send_email_verification(user['idToken']

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
            print(e)

    def signup_as_seller(self,email,password,name="",country="",city="",address="",postal_code="",service_number="",logo=""):
        try:
            # Set User Type
            account_location="sellers"

            # Create New User
            user=self.auth.create_user_with_email_and_password(email,password)

            # Verify Email Address
            #auth.send_email_verification(user['idToken']

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
                raise Exception(message="User does not exist!")
        except HTTPError as e:
            return e

    def login_as_seller(self,email,password):
        try:
            # Validate Status as Seller
            if self.db.collection('sellers').document(email).get().exists:
        
                # Sign In the User
                user = self.auth.sign_in_with_email_and_password(email,password)
        
                return user
            else: 
                raise Exception(message="User does not exist!")
        except HTTPError as e:
            return json.loads(e.strerror)


    def testDB(self):
        results = self.db.collection('buyers').document('test@gmail.com').get()
        print(results.to_dict())


        