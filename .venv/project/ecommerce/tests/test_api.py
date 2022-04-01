"""this module contains tests for the various APIs
"""
from django.test import TestCase
from firebase_admin import firestore
from ..api.itembrowsing import item_collection_to_dict

class TestItemBorwsing(TestCase):
    """contains tests for the item browsing api
    """
    def test_better_than_score(self):
        """test the better than score gets the items with a given score
        """
        database = firestore.client()
        items_ref=database.collection('items')
        itemsreviewed=items_ref.where('score', '<', 'score')
        itemsreviewed_worse_than=items_ref.where('score', '>', 'score')
        self.assertIsNotNone(itemsreviewed)
        self.assertNotEqual(itemsreviewed,itemsreviewed_worse_than)
    def test_worse_than_score(self):
        """test if the test worse than score gets descending order for items
        """
        database = firestore.client()
        items_ref=database.collection('items')
        itemsreviewed=items_ref.where('score', '>', 'score')
        self.assertIsNotNone(itemsreviewed)

    def test_get_categories(self):
        """test if the get categories function gets all categories
        """
        database = firestore.client()
        category_names_ref=database.collection('Categories').document('names')
        category_names_dict = category_names_ref.get().to_dict()
        self.assertIsNotNone(category_names_dict['names'])

    def test_get_all_items(self):
        """test if the get all items function gets items
        """
        database = firestore.client()
        items_ref=database.collection('items')
        all_items_ref = items_ref.stream()
        all_items:list = item_collection_to_dict(all_items_ref)
        self.assertIsNotNone(all_items)
        