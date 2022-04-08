"""
Module contains information for user payment information
"""
import hashlib
from ecommerce.api.banking_info import *


class PaymentInfo():
    """
    Saves payment information of either buyers or sellers
    """

    def __init__(self,email,buyer_payment_data=None,seller_payment_data=None):
        """
        """

        self.email = email

        if buyer_payment_data is not None:
            self.firstname = buyer_payment_data['firstname']
            self.lastname = buyer_payment_data['lastname']
            self.number = hashlib.md5(buyer_payment_data['number'].encode()).hexdigest()
            self.expiration_date=buyer_payment_data['expirationDate']
            self.cvv = hashlib.md5(buyer_payment_data['cvv'].encode()).hexdigest()
            self.is_buyer=True

        if seller_payment_data is not None:
            self.is_buyer=False
            self.transit = hashlib.md5(seller_payment_data['transit'].encode()).hexdigest()
            self.institution = hashlib.md5(seller_payment_data['institution'].encode()).hexdigest()
            self.account = hashlib.md5(seller_payment_data['account'].encode()).hexdigest()

    def save(self):
        """save the payment information for buyers and sellers
        """
        if self.is_buyer:
            add_payment_info_buyer(
                email=self.email,
                first_name=self.firstname,
                last_name=self.lastname,
                number=self.number,
                expiration_date=self.expiration_date,
                cvv=self.cvv
            )
        else:
            add_payment_info_seller(
                email=self.email,
                transit=self.transit,
                institution=self.institution,
                account=self.account
            )
    