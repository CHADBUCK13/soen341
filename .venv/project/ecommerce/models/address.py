class Address():
    def __init__(self, country:str, city:str, streetAddress:str, postalCode:str):
        self.country = country
        self.city = city
        self.streetAddress = streetAddress
        self.postalCode = postalCode 
    
    def to_json(self):
        return {'country': self.country, 'city': self.city, 'streetAddress': self.streetAddress, 'postalCode': self.postalCode}
    
    def from_json(dict):
        return Address(dict['country'], dict['city'], dict['streetAddress'], dict['postalCode'])
        