#
#  Object-Oriented Python: Advanced Objects
#  Python Techdegree
#
#  Created by Dulio Denis on 12/16/18.
#  Copyright (c) 2018 ddApps. All rights reserved.
# ------------------------------------------------
#  Final Challenge Task 1 of 1
#  We need to be able to set the price of a product through a property setter.
#  Add a new setter (@price.setter) method to the Product class that updates the _price attribute. 
class Product:
    _price = 0.0
    tax_rate = 0.12
  
    def __init__(self, base_price):
        self._price = base_price
    
    @property
    def price(self):
        return self._price + (self._price * self.tax_rate)

    @price.setter
    def price(self, price):
        self._price = price

p = Product(12)
print(p.price)
p.price = 15
print(p.price)