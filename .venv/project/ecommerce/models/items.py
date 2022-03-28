"""
Contains Item, Category and Rating class
"""

from difflib import SequenceMatcher


class Item:
    """
    Item that can be put on sale.
    """

    def __init__(
        self, add_item_form_data=None, item_data=None, seller_id=None, photo=None
    ):
        """
        Creates a new Item instance.
        """

        # Create the Item with the info from the addItem Form
        if add_item_form_data is not None:
            self.name = add_item_form_data["name"]
            self.price = add_item_form_data["price"]
            self.description = add_item_form_data["description"]
            self.weight = add_item_form_data["weight"]
            self.category = Category(
                category_name=add_item_form_data["category"],
                related_categories=add_item_form_data["relatedCategories"],
            )
            self.numberofreviews = 0
            self.score = 0
            self.sales = False
            self.photo = photo

        if item_data is not None:
            self.category = Category(
                category_name=item_data["category"]["category_name"],
                related_categories=item_data["category"]["relatedcategory"],
            )
            self.description = item_data["description"]
            self.name = item_data["name"]
            self.photo = item_data["photo"]
            self.price = item_data["price"]
            self.numberofreviews = item_data["rating"]["numberofreviews"]
            self.score = item_data["rating"]["score"]
            self.seller_id = item_data["sellerID"]
            self.weight = item_data["weight"]
            self.sales = item_data["sales"]
            self.id = item_data["id"]

        if seller_id is not None:
            self.seller_id = seller_id
        else:
            self.seller_id = ""

    def match(self, search_text=""):
        """
        Looks for match between
        """
        acceptance_ratio = 0.5

        if (
            SequenceMatcher(None, self.category.category_name, search_text).ratio()
            >= acceptance_ratio
        ):
            return True
        if (
            SequenceMatcher(None, self.category.related_categories, search_text).ratio()
            >= acceptance_ratio
        ):
            return True
        if SequenceMatcher(None, self.name, search_text).ratio() >= acceptance_ratio:
            return True
        if (
            SequenceMatcher(None, self.description, search_text).ratio()
            >= acceptance_ratio
        ):
            return True

        return False

    def to_dict(self):
        """
        Converts item obejct to dictionary
        """
        dictionary = {
            "name": self.name,
            "price": self.price,
            "description": self.description,
            "weight": self.weight,
            "category": {
                "category_name": self.category.category_name,
                "relatedcategory": self.category.related_categories,
            },
            "rating": {"numberofreviews": self.numberofreviews, "score": self.score},
            "sales": self.sales,
            "photo": self.photo,
            "sellerID": self.seller_id,
        }
        return dictionary


class Category:
    """
    Class describing database category
    """
    def __init__(self, category_name, related_categories):
        self.category_name = category_name
        self.related_categories = related_categories


class Rating:
    """
    Class describing database rating
    """
    def __init__(self, user_id="", date=0, score=0, review=""):
        self.user_id = user_id
        self.date = date
        self.score = score
        self.review = review
