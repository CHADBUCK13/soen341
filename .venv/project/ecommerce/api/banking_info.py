"""
This module contains all the logic required for buyer and seller banking info
"""

from firebase_admin import firestore

db = firestore.client()
payments_ref = db.collection('paymentsInfo')

def add_payment_info_buyer(email,first_name="",last_name="",number="",expiration_date="",cvv=""):
    """
    Save the Buyer's Payment Info to the DB.
    """

    payment_data = {
        'name': {'first':first_name,'last':last_name,},
        'number':number,
        'expirationDate':expiration_date,
        'cvv':cvv,
        'valid': True
    }

    payment_info_path = 'buyers/'+email+"/payment_information"
    db.collection(payment_info_path).add(payment_data)

def add_payment_info_seller(email,transit="",institution="",account=""):
    """
    Save the Seller's Payment Info to the DB.
    """

    payment_data={
        'transit':transit,
        'institution':institution,
        'account':account
    }

    payments_ref.document(email).set(payment_data)

def has_payment_info(email):
    """
    Returns True if the given User has Payment Info in the DB.
    """
    return payments_ref.document(email).get().exists
