from google.cloud import firestore 
#updated linked frontend to backend 
db = firestore.Client()

#reference to items collections
items_ref=db.collection(u'items')

def addItems(self,name="",sellerID=0,photo="",price=0,description="",weight=0,rating=0, score=0,sales=False,category=None):

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
    

#search for items based on price range
def order_by_price(min=0, max=0):

    price_ref=items_ref.order_by_child('price').start_at(min).end_at(max).get()
    print(price_ref)

#find related categories of a given category
def categories(category=""):
 
    categories = items_ref.order_by_child(category)
    related = categories.order_by_child('relatedcategories')
    for key in related.items():
        print(key)

#get all categories
def get_categories():

    categoryNamesRef=db.collection(u'Categories').document(u'names')
    categoryNamesDict = categoryNamesRef.get().to_dict()
    return categoryNamesDict['names']

#search all categories
def get_all_items(numberOfItems = 0):
    allItemsRef = items_ref.stream()
    allItems = []

    for itemDoc in allItemsRef:
        #print(f'{itemDoc.id} => {itemDoc.to_dict()}')
        allItems.append(itemDoc.to_dict())

    

    return allItems

def get_items_by_category(category = "", numberOfItems=0):
    itemsRef = items_ref.where(u'category', u'==', category).limit(numberOfItems).stream()
    allItems = []

    for itemDoc in itemsRef:
        allItems.append(itemDoc.to_dict())

    return allItems

#get all items with a certain number of sales
def get_items_on_sale(numberOfItems):
    itemsRef = items_ref.where(u'sale', u'==', u'True').order_by('name').limit(numberOfItems).stream()
    allItems = {}

    for itemDoc in itemsRef:
        allItems.update(itemDoc.to_dict())

    return allItems

#add reviews to items

#get items with a given score
def better_than_score(self, score):

    items_ref=db.collection(u'items')

    itemsreviewed=items_ref.where(u'score', u'<', u'score')

    print(itemsreviewed)


     
