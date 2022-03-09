from ..api.bankingInfo import *
import hashlib

class PaymentInfo():
    """
    """

    def __init__(self,email,buyer_payment_data=None,seller_payment_data=None):
        """
        """

        self.email = email

        if buyer_payment_data is not None:
            self.firstname = buyer_payment_data['firstname']
            self.lastname = buyer_payment_data['lastname']
            self.number = hashlib.md5(buyer_payment_data['number'].encode()).hexdigest()
            self.expirationDate=buyer_payment_data['expirationDate']
            self.cvv = hashlib.md5(buyer_payment_data['cvv'].encode()).hexdigest()
            self.isBuyer=True

        if seller_payment_data is not None:
            self.isBuyer=False
            self.transit = hashlib.md5(seller_payment_data['transit'].encode()).hexdigest()
            self.institution = hashlib.md5(seller_payment_data['institution'].encode()).hexdigest()
            self.account = hashlib.md5(seller_payment_data['account'].encode()).hexdigest()

    def save(self):
        if self.isBuyer:
            addPaymentInfoBuyer(
                email=self.email,
                firstName=self.firstname,
                lastName=self.lastname,
                number=self.number,
                expirationDate=self.expirationDate,
                cvv=self.cvv
            )
        else:
            addPaymentInfoSeller(
                email=self.email,
                transit=self.transit,
                institution=self.institution,
                account=self.account
            )
    