"""
This module contains all the logic required for buyer checkout
"""
import datetime
from firebase_admin import firestore
from google.cloud import firestore as fs
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from ecommerce.models.order import Order
from ecommerce.models.payment_information import PaymentInformation


db = firestore.client()


def get_payment_info(email: str):
    """
    Returns collection of PaymentInformation if available, if not returns empty list.
    Should any of the values be incorrect the PaymentInfo returned will have valid=False flag.
    """
    payment_info_path = "buyers/" + email + "/payment_information"
    payments = db.collection(payment_info_path).stream()
    all_payments = []

    for card in payments:
        card_dict = card.to_dict()
        expiration_date = datetime.datetime.strptime(
            card_dict["expirationDate"], "%m%y"
        ).date()

        try:
            payment_info = PaymentInformation(
                card_dict["name"]["first"],
                card_dict["name"]["last"],
                card_dict["number"],
                expiration_date,
                card_dict["cvv"],
                True,
            )

            all_payments.append(payment_info)
        except ValueError:
            payment_info = PaymentInformation(
                card_dict["name"]["first"],
                card_dict["name"]["last"],
                card_dict["number"],
                expiration_date,
                card_dict["cvv"],
                False,
            )
            all_payments.append(payment_info)

    return all_payments


def check_out(email: str, order: Order):
    """
    Takes the Order, selected PaymentInformation and email of the user checking out.
    Returns True if the checkout was successful, False otherwise
    """
    order_data = order.to_dict()
    orders_path = "buyers/" + email + "/orders"
    order_ref = db.collection(orders_path).document()
    order_ref.set(order_data)
    order.id = order_ref.id

    clear_shopping_cart(email)
    send_confirmation_email(order_ref.id, order, email)


def cancel_order(email: str, order_id: str):
    """
    Takes user email and orderID to be cancelled and sets the order to cancelled
    """

    orders_path = "buyers/" + email + "/orders"
    order_ref = db.collection(orders_path).document(order_id)

    order_ref.update({"cancelled": True})

    return True


def get_orders(email: str, number_of_orders: int):
    """
    Takes user email and number of orders desired and returns a list of Order
    """
    orders_path = "buyers/" + email + "/orders"
    orders_ref = (
        db.collection(orders_path)
        .order_by("date", direction=fs.Query.DESCENDING)
        .limit(number_of_orders)
        .stream()
    )
    all_orders = []

    for order_doc in orders_ref:
        order = Order.from_document_reference(None, order_doc)
        all_orders.append(order)

    return all_orders


# Helper functions
def send_confirmation_email(order_id, order, email):
    """
    Sends order confirmation email to specified email
    """
    mail_subject = "Order#" + order_id + " Confirmation"
    message = render_to_string(
        "order_confirmation_email.html", {"order": order, "email": email}
    )
    email = EmailMultiAlternatives(subject=mail_subject, body="", to=[email])
    email.attach_alternative(message, "text/html")
    email.send()


def clear_shopping_cart(email: str):
    """
    Removes all items from database cart of email specified
    """
    data = {"items": {}}
    shopping_cart_ref = db.collection("shopping_cart").document(email)
    shopping_cart_ref.set(data)
