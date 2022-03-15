from ..api import itembrowsing
from difflib import SequenceMatcher

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
            self.numberofreviews = 0
            self.score = 0
            self.sales = False 
            self.photo= photo

        if item_data is not None:
            self.category = Category(category_name=item_data['category']['category_name'],related_categories=item_data['category']['relatedcategory'])
            self.description = item_data['description']
            self.name=item_data['name']
            self.photo=item_data['photo']
            self.price=item_data['price']
            self.numberofreviews = item_data['rating']['numberofreviews']
            self.score=item_data['rating']['score']
            self.sellerID=item_data['sellerID']
            self.weight=item_data['weight']

        if sellerID is not None:
            self.sellerID = sellerID
    
    def save(self):
        """
        Saves the current Item in the DB.
        """
        itembrowsing.addItems(
            name=self.name,
            sellerID=self.sellerID,
            photo=self.photo,
            price=self.price,
            description=self.description,
            weight=self.weight,
            score=self.score,
            sales=self.sales,
            category=Category(self.category,self.relatedCategories))

    def match(self,searchText=""):
        ACCEPTANCE_RATIO = 0.5

        if SequenceMatcher(None,self.category.category_name,searchText).ratio() >= ACCEPTANCE_RATIO: 
            return  True
        if SequenceMatcher(None,self.category.related_categories,searchText).ratio() >= ACCEPTANCE_RATIO:
            return True
        if SequenceMatcher(None,self.name,searchText).ratio() >= ACCEPTANCE_RATIO:
            return True
        if SequenceMatcher(None,self.description,searchText).ratio() >= ACCEPTANCE_RATIO:
            return True

        return False



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

