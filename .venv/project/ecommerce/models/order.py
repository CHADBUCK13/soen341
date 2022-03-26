"""
Contains Order class only
"""

import datetime

from ecommerce.models.address import Address


class Order:
    """
    Describes database order and contains related functions
    """
    def __init__(
        self,
        subtotal: float,
        total: float,
        n_of_items: int,
        cancelled: bool,
        payment_info: str,
        items: dict,
        date: datetime,
        time: datetime,
        shipping_address: Address,
        billing_address: Address,
        id="",
    ):
        self.subtotal = subtotal
        self.total = total
        self.n_of_items = n_of_items
        self.cancelled = cancelled
        self.payment_info = payment_info
        self.items = items
        self.date = date
        self.time = time
        self.shipping_address = shipping_address
        self.billing_address = billing_address
        self.id = id

    def to_dict(self):
        """
        Converts order object to dictionary
        """
        order_data = {
            "subtotal": self.subtotal,
            "total": self.total,
            "nOfItems": self.n_of_items,
            "cancelled": self.cancelled,
            "paymentInfo": self.payment_info,
            "items": self.items,
            "date": self.date.strftime("%y/%m/%d"),
            "time": self.time.strftime("%H:%M:%S"),
            "shippingAddress": self.shipping_address.to_dict(),
            "billingAddress": self.billing_address.to_dict(),
        }

        return order_data

    def from_document_reference(self, order_doc):
        """
        Converts firebase order document reference to Order object and returns it
        """
        order_dict = order_doc.to_dict()
        date = datetime.datetime.strptime(order_dict["date"], "%y/%m/%d").date()
        time = datetime.datetime.strptime(order_dict["time"], "%H:%M:%S").time()
        shipping_address = Address.from_dict(self, order_dict["shippingAddress"])
        billing_address = Address.from_dict(self, order_dict["billingAddress"])

        print(order_dict["items"])
        return Order(
            order_dict["subtotal"],
            order_dict["total"],
            order_dict["nOfItems"],
            order_dict["cancelled"],
            order_dict["paymentInfo"],
            order_dict["items"],
            date,
            time,
            shipping_address,
            billing_address,
            order_doc.id,
        )
