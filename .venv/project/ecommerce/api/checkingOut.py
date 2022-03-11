from datetime import date
import datetime
from firebase_admin import firestore
from ecommerce.models.order import Order
from ecommerce.models.paymentInformation import PaymentInformation, CardNumber
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives

db = firestore.client()

def get_payment_info(email:str):
    """
    Returns collection of PaymentInformation if available, if not returns empty list. Should any of the values be incorrect the PaymentInfo returned will have valid=False flag.
    """
    paymentInfoPath = 'buyers/'+email+"/payment_information"
    payments=db.collection(paymentInfoPath).stream()
    allPayments = []

    for card in payments:
        cardDict = card.to_dict()
        expirationDate = datetime.datetime.strptime(cardDict['expiration_date'], "%m/%y").date()

        try:
            number = CardNumber(cardDict['number'])
            paymentInfo = PaymentInformation(cardDict['name']['first'],cardDict['name']['last'],number,expirationDate,cardDict['CVV'],True)

            allPayments.append(paymentInfo)
        except ValueError:
            paymentInfo = PaymentInformation(cardDict['name']['first'],cardDict['name']['last'],number,expirationDate,cardDict['CVV'],False)
            allPayments.append(paymentInfo)

    return allPayments

def check_out(email:str, order:Order):
    """
    Takes the Order, selected PaymentInformation and email of the user checking out. Returns True if the checkout was successful, False otherwise
    """
    orderData = {
        "subtotal": order.subtotal,
        "total": order.total,
        "nOfItems": order.nOfItems,
        "cancelled": order.cancelled,
        "paymentInfo": order.paymentInfo,
        "items": order.items
    }

    paymentInfoPath = 'buyers/'+email+"/orders"
    orderRef = db.collection(paymentInfoPath).document()
    orderRef.set(orderData)

    clear_shopping_cart(email)
    send_confirmation_email(orderRef.id, order, email)

def send_confirmation_email(id, order, email):
    mail_subject = 'Order#' + id + ' Confirmation'
    message = render_to_string('order_confirmation_email.html', {
        'order': order,
        'email': email
    })
    email = EmailMultiAlternatives(
        subject=mail_subject, body="", to=[email]
    )
    email.attach_alternative(message, "text/html")
    email.send()

    
    
def clear_shopping_cart(email:str):
    data = {}
    shoppingCartRef = db.collection("shopping_cart").document(email)
    shoppingCartRef.set(data)