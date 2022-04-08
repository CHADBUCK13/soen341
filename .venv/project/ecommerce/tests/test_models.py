"""Contains the tests for the user models
"""
from django.test import TestCase
from ecommerce.models.buyer import Buyer
from ecommerce.models.seller import Seller


class TestBuyerModel(TestCase):
    """contains the tests for the buyer model
    """

    def test_account_type(self):
        """test that the buyer account is associated with the correct type
        """
        self.assertEqual(Buyer.account_type(self), "buyer")


class TestSellerModel(TestCase):
    """contains the tests for the seller model
    """

    def test_account_type(self):
        """Test that the seller account is associated with the correct type
        """
        self.assertEqual(Seller.account_type(self), "seller")
