import json
import os
import py_compile
import firebase_admin
from firebase_admin import credentials

credJSON = os.getenv('GOOGLE_APPLICATION_CREDENTIALS')
credDict = json.loads(credJSON)

cred = credentials.Certificate(credDict)

# Firebase Firestore Database connection
firebase_admin.initialize_app(credential=cred)
from ecommerce.api.itemBrowsingV2 import get_items_on_sale

x = get_items_on_sale(1)
print(x)

attrs = vars(x[0])
print(', '.join("%s: %s" % item for item in attrs.items()))


#from ecommerce.shoppingCartBetter import get_items_from_cart
#email = ""
#x = get_items_from_cart(email)
#print(x)""

