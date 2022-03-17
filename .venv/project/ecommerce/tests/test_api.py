from django.test import TestCase
from firebase_admin import firestore
from ..api.itembrowsing import order_by_price,better_than_score,worse_than_score,get_categories,get_all_items,get_all_items_dict,get_items_by_search,item_collection_to_dict

class TestItemBorwsing(TestCase):


    def test_better_than_score(self):
        db = firestore.client()
        items_ref=db.collection(u'items')
        itemsreviewed=items_ref.where(u'score', u'<', u'score')
        self.assertIsNotNone(itemsreviewed)
    
    def test_worse_than_score(self):
        db = firestore.client()
        items_ref=db.collection(u'items')
        itemsreviewed=items_ref.where(u'score', u'>', u'score')
        self.assertIsNotNone(itemsreviewed)
    
    def test_get_categories(self):
        db = firestore.client()
        categoryNamesRef=db.collection(u'Categories').document(u'names')
        categoryNamesDict = categoryNamesRef.get().to_dict()
        self.assertIsNotNone(categoryNamesDict['names'])
   
    def test_get_all_items(self):
        db = firestore.client()
        items_ref=db.collection(u'items')
        allItemsRef = items_ref.stream()
        allItems:list = item_collection_to_dict(allItemsRef)
        self.assertIsNotNone(allItems)