
from datetime import date


class Order():
    def __init__(self, subtotal:float, total:float, nOfItems:int, cancelled:bool, paymentInfo:str, items:dict, date:date, time:date, id = ""):
        self.subtotal = subtotal
        self.total = total
        self.nOfItems = nOfItems
        self.cancelled = cancelled
        self.paymentInfo = paymentInfo
        self.items = items
        self.date = date
        self.time = time
        self.id = id