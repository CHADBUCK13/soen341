from firebase_admin import firestore
from firebase_admin import db
from google-cloud-firestore 

class Item_Queries ():

    def addItems(self,name="",sellerID=0,photo="",price=0,description="",weight=0,rating=0, score=0,review="", userID="", date=0, numberofreviews=0,sales=False,category=None):

        itemlocation = "items"

        items_data = {
                'name':name,
                'sellerID':sellerID,
                'photo':photo,
                'price':price,
                'description':description,
                'weight':weight,
                'sales':sales,
                'rating': {
                    'score':score,   
                    'numberofreviews':0        
                },
                'category': {
                    'category_name' : category.category_name,
                    'relatedcategory': category.related_categories
                }
             }

        self.db.collection(itemlocation).document(name).set(items_data)
#reference to items, should be able to read all items
    items_ref=db.reference('items')
    

#search for items based on price range
def order_by_price(min=0, max=0):

    items_ref=db.reference('items')
    price_ref=items_ref.order_by_child('price').start_at(min).end_at(max).get()

    print(price_ref)

#find related categories of a given category
def categories(category=""):

    items_ref=db.reference('items')
    categories = items_ref.order_by_child(category)
    related = categories.order_by_child('relatedcategories')

    for key in related.items():
        print(key)

#search all categories
def all_category():

    items_ref=db.reference('items')
    allcategories=items_ref.order_by_child('category/name').get()

    print(allcategories)

#get all items with a certain number of sales
def is_on_sale(self, sales=False):

    items_ref=db.reference('items')
    sales=items_ref.order_by_child('sales').equal_to(sales).get()

    print(sales)

#add reviews to items

#get items with a given score
def better_than_score(self, score):

    items_ref=db.collection(u'items')

    itemsreviewed=items_ref.where(u'score', u'<', u'score')


    order_by_child('rating/score').equal_to(score).get()

    print(itemsreviewed)

def worse_than_score()


     
