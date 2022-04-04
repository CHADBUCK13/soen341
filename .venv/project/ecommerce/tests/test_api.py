"""this module contains tests for the various APIs
"""
import json
from django.test import TestCase
import pyrebase
from firebase_admin import firestore
from ..api.itembrowsing import item_collection_to_dict


class TestItemBorwsing(TestCase):
    """contains tests for the item browsing api
    """

    def test_better_than_score(self):
        """test the better than score gets the items with a given score
        """
        database = firestore.client()
        items_ref = database.collection('items')
        itemsreviewed = items_ref.where('score', '<', 'score')
        itemsreviewed_worse_than = items_ref.where('score', '>', 'score')
        self.assertIsNotNone(itemsreviewed)
        self.assertNotEqual(itemsreviewed, itemsreviewed_worse_than)

    def test_worse_than_score(self):
        """test if the test worse than score gets descending order for items
        """
        database = firestore.client()
        items_ref = database.collection('items')
        itemsreviewed = items_ref.where('score', '>', 'score')
        self.assertIsNotNone(itemsreviewed)

    def test_get_categories(self):
        """test if the get categories function gets all categories
        """
        database = firestore.client()
        category_names_ref = database.collection(
            'Categories').document('names')
        category_names_dict = category_names_ref.get().to_dict()
        self.assertIsNotNone(category_names_dict['names'])

    def test_get_all_items(self):
        """test if the get all items function gets items
        """
        database = firestore.client()
        items_ref = database.collection('items')
        all_items_ref = items_ref.stream()
        all_items: list = item_collection_to_dict(all_items_ref)
        self.assertIsNotNone(all_items)


class TestAccountContext(TestCase):
    """Tests for account context
    """

    def setUp(self):
        self.email_seller = "seller@gmail.com"
        self.email_buyer = "test@gmail.com"
        self.password = "Django1234"
        self.firebae_config = json.load(
            open("pyrebaseConfig.json", encoding="utf-8"))
        self.auth = pyrebase.initialize_app(self.firebae_config).auth()

        self.seller = self.auth.sign_in_with_email_and_password(
            self.email_seller, self.password)
        self.buyer = self.auth.sign_in_with_email_and_password(
            self.email_seller, self.password)

        return super().setUp()

    def test_login_as_seller_valid_data(self):
        """Test if the user can login as seller using a valid email and passwrord, test is_seller
        """
        database = firestore.client()
        self.assertTrue(database.collection(
            "sellers").document(self.email_seller).get().exists)
        self.assertTrue(self.seller)

    def test_login_as_buyer_valid_data(self):
        """Test if the user can login as buyer using a valid email and passwrord, test is_buyer
        """
        database = firestore.client()
        self.assertTrue(database.collection(
            "buyers").document(self.email_buyer).get().exists)
        self.assertTrue(self.buyer)

    def test_reset_password_valid_email(self):
        """test if the reset password email is being sent with a valid email
        """
        self.assertTrue(self.auth.send_password_reset_email(self.email_seller))
