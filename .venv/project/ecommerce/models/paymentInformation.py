from datetime import date
import re

class CardNumber():
    def __init__(self, number:str):
        PATTERN='^(?:4[0-9]{12}(?:[0-9]{3})?|(?:5[1-5][0-9]{2}| 222[1-9]|22[3-9][0-9]|2[3-6][0-9]{2}|27[01][0-9]|2720)[0-9]{12}|3[47][0-9]{13}|3(?:0[0-5]|[68][0-9])[0-9]{11}|6(?:011|5[0-9]{2})[0-9]{12}|(?:2131|1800|35\d{3})\d{11})$'
        
        if(re.search(PATTERN, number)):
            self.number = number
        else:
            raise ValueError('Invalid Number') 
            
class PaymentInformation():
    def __init__(self, first:str, last:str, number:str, expirationDate:date, CVV:int, valid:bool):
        self.first = first
        self.last = last
        self.number = number
        self.expirationDate = expirationDate
        self.CVV = CVV
        self.valid = valid


