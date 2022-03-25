import datetime

from ecommerce.models.address import Address


class Order():
    def __init__(self, subtotal:float, total:float, nOfItems:int, cancelled:bool, paymentInfo:str, items:dict, date:datetime, time:datetime, shippingAddress:Address, billingAddress:Address, id = ""):
        self.subtotal = subtotal
        self.total = total
        self.nOfItems = nOfItems
        self.cancelled = cancelled
        self.paymentInfo = paymentInfo
        self.items = items
        self.date = date
        self.time = time
        self.shippingAddress = shippingAddress
        self.billingAddress = billingAddress
        self.id = id
    
    def to_dict(self):
        orderData = {
            "subtotal": self.subtotal,
            "total": self.total,
            "nOfItems": self.nOfItems,
            "cancelled": self.cancelled,
            "paymentInfo": self.paymentInfo,
            "items": self.items,
            "date": self.date.strftime("%y/%m/%d"),
            "time": self.time.strftime("%H:%M:%S"),
            'shippingAddress': self.shippingAddress.to_dict(),
            'billingAddress': self.billingAddress.to_dict()
        }

        return orderData
    
    def from_documentReference(orderDoc):

        orderDict = orderDoc.to_dict()
        date = datetime.datetime.strptime(orderDict['date'], "%y/%m/%d").date()
        time = datetime.datetime.strptime(orderDict['time'], "%H:%M:%S").time()
        shippingAddress = Address.from_dict(orderDict['shippingAddress'])
        billingAddress = Address.from_dict(orderDict['billingAddress'])

        print(orderDict['items'])
        return Order(orderDict['subtotal'], orderDict['total'], orderDict['nOfItems'], orderDict['cancelled'], orderDict['paymentInfo'], orderDict['items'], date, time, shippingAddress, billingAddress, orderDoc.id)