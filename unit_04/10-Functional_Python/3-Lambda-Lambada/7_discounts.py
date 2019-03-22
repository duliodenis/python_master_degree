#
#  Functional Python: The Lambda Lambada (Partials)
#  Python Techdegree
#
#  Created by Dulio Denis on 3/22/19.
#  Copyright (c) 2019 ddApps. All rights reserved.
# ------------------------------------------------
#  Partial Challenge
# ------------------------------------------------
#  Challenge Task 1 of 4
#  First, import partial from functools.
from functools import partial

prices = [
    10.50,
    9.99,
    0.25,
    1.50,
    8.79,
    101.25,
    8.00
]

def discount(price, amount):
    return price - price * (amount/100)

# ------------------------------------------------
#  Challenge Task 2 of 4
#  Now, use partial to make a version of discount
#  that applies a 10% discount.
#  Name this partial function discount_10.
discount_10 = partial(discount, amount=10)

# ------------------------------------------------
#  Challenge Task 3 of 4
#  Great! Follow that same pattern to make discount_25
#  and discount_50 with 25% and 50% discounts each.
discount_25 = partial(discount, amount=25)
discount_50 = partial(discount, amount=50)

# ------------------------------------------------
#  Challenge Task 4 of 4
#  Finally, I need to see all of our prices with each
#  discount applied.
#  Use map() to create prices_10, prices_25, and prices_50
#  where you discount all of the prices with the appropriate discount.
prices_10 = map(discount_10, prices)
prices_25 = map(discount_25, prices)
prices_50 = map(discount_50, prices)

print(list(prices_10))
print(list(prices_25))
print(list(prices_50))
