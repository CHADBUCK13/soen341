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
        "items": order.items,
        "date": order.date,
        "time": order.time,
        "id": order.id
    }

    ordersPath = 'buyers/'+email+"/orders"
    orderRef = db.collection(ordersPath).document()
    orderRef.set(orderData)
    order.id = orderRef.id

    clear_shopping_cart(email)
    send_confirmation_email(orderRef.id, order, email)

def cancel_order(email:str, orderID:str):
    """
    Takes user email and orderID to be cancelled and sets the order to cancelled
    """
    
    ordersPath = 'buyers/'+email+"/orders"
    orderRef = db.collection(ordersPath).document(orderID)
    
    orderRef.update({'cancelled': True})

    return True

def get_orders(email:str, numberOfOrders:int):
    """
    Takes user email and number of orders desired and returns a list of Order
    """
    ordersPath = 'buyers/'+email+"/orders"
    ordersRef = db.collection(ordersPath).order_by('date', direction=firestore.Query.DESCENDING).limit(numberOfOrders).stream()
    allOrders = []

    for orderDoc in ordersRef:
        orderDict = orderDoc.to_dict()
        date = datetime.datetime.strptime(orderDict['date'], "%y/%m/%d").date()
        time = datetime.datetime.strptime(orderDict['time'], "%H:%M:%S").time()
        order = Order(orderDict['subtotal'], orderDict['total'], orderDict['nOfItems'], orderDict['cancelled'], orderDict['paymentInfo'], orderDict['items'], date, time, orderDoc.id)
        allOrders.append(order)

    return allOrders
    

#Helper functions
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