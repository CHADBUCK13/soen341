from ..api.itembrowsing import *

class Item():
    """
    Item that can be put on sale.
    """

    def __init__(self, add_item_form_data=None, item_data=None, sellerID=None,photo=None):
        """
        Creates a new Item instance.
        """    
        
        # Create the Item with the info from the addItem Form
        if add_item_form_data is not None:
            self.name = add_item_form_data['name']
            self.price = add_item_form_data['price']
            self.description = add_item_form_data['description']
            self.weight = add_item_form_data['weight']
            self.category = add_item_form_data['category']
            self.relatedCategories = add_item_form_data['relatedCategories']
            self.amountInStock = add_item_form_data['amount']
            self.numberofreviews = 0
            self.score = 0
            self.sales = False 
            self.photo= photo

        if item_data is not None:
            pass

        if sellerID is not None:
            self.sellerID = sellerID
    
    def save(self):
        """
        Saves the current Item in the DB.
        """
        addItems(
            name=self.name,
            sellerID=self.sellerID,
            photo=self.photo,
            price=self.price,
            description=self.description,
            weight=self.weight,
            score=self.score,
            sales=self.sales,
            amountInStock=self.amountInStock,
            category=Category(self.category,self.relatedCategories))


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
