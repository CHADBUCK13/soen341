import socketserver
from unicodedata import name


class Item:
    def __init__(self,name,sellerID=0,photo=None,price=0,description=None,weight=0,score=0,numberofreviews=0,sales=[],category=None):
        self.name=name
        self.sellerID=sellerID
        self.photo=photo
        self.price=price
        self.description=description
        self.weight=weight
        self.score=score
        self.numberofreviews=numberofreviews
        self.sales=sales
        self.category=category


class Category:
    def __init__(self, category_name, related_categories):
        self.category_name = category_name
        self.related_categories = related_categories


class Rating:
    def __init__(self, userID="", date=0, score=0, review=""):
        self.userID = userID
        self.date = date
        self.score = score
        self.review =review
