"""This module includes the tests for the models
"""
from django.test import TestCase
from ..models.buyer import Buyer
from ..models.seller import Seller


class TestBuyerModel(TestCase):
    """tests for the buyer model
    """

    def test_account_type(self):
        """test if the buyer model returns the correct account type
        """
        self.assertEqual(Buyer.accountType(self), "buyer")


class TestSellerModel(TestCase):
    """tests for the seller model
    """
    def test_account_type(self):
        """test if the seller model returns the correct account type
        """
        self.assertEqual(Seller.accountType(self), "seller")
