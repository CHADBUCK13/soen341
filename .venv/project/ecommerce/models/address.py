"""
Contains Address class only
"""


class Address:
    """
    Class describing user adrress
    """

    def __init__(self, country: str, city: str, street_address: str, postal_code: str):
        self.country = country
        self.city = city
        self.street_address = street_address
        self.postal_code = postal_code

    def to_dict(self):
        """
        Converts object to dictionary
        """
        return {
            "country": self.country,
            "city": self.city,
            "streetAddress": self.street_address,
            "postalCode": self.postal_code,
        }

    def from_dict(self, dictionary: dict):
        """
        Takes dictionary describing address and returns address object
        """
        return Address(
            dictionary["country"],
            dictionary["city"],
            dictionary["streetAddress"],
            dictionary["postalCode"],
        )
