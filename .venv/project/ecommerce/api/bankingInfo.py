from firebase_admin import firestore

db = firestore.client()
payments_ref = db.collection(u'paymentsInfo')

def addPaymentInfoBuyer(email,firstName="",lastName="",number="",expirationDate="",cvv=""):
    """
    Save the Buyer's Payment Info to the DB.
    """

    payment_data = {
        'name': {'first':firstName,'last':lastName,},
        'number':number,
        'expirationDate':expirationDate,
        'cvv':cvv,
        'valid': True
    }

    paymentInfoPath = 'buyers/'+email+"/payment_information"
    db.collection(paymentInfoPath).add(payment_data)

def addPaymentInfoSeller(email,transit="",institution="",account=""):
    """
    Save the Seller's Payment Info to the DB.
    """

    payment_data={
        'transit':transit,
        'institution':institution,
        'account':account
    }

    payments_ref.document(email).set(payment_data)

def hasPaymentInfo(email):
    """
    Returns True if the given User has Payment Info in the DB.
    """
    return payments_ref.document(email).get().exists
