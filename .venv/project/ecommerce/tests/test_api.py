from django.test import TestCase
from ..databaseContext import DatabaseContext
from firebase_admin import firestore
from ..api import itembrowsing

class TestItemBorwsing(TestCase):


    def test_better_than_score(self):
        db = firestore.client()
        items_ref=db.collection(u'items')
        itemsreviewed=items_ref.where(u'score', u'<', u'score')
        self.assertIsNotNone(itemsreviewed)
    