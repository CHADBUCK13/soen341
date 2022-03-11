
class Order():
    def __init__(self, subtotal:float, total:float, nOfItems:int, cancelled:bool, paymentInfo:str, items:dict):
        self.subtotal = subtotal
        self.total = total
        self.nOfItems = nOfItems
        self.cancelled = cancelled
        self.paymentInfo = paymentInfo
        self.items = items