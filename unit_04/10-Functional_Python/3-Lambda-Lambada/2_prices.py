#
#  Functional Python: The Lambda Lambada (Reduce)
#  Python Techdegree
#
#  Created by Dulio Denis on 3/22/19.
#  Copyright (c) 2019 ddApps. All rights reserved.
# ------------------------------------------------
#  Reduce Challenge
# ------------------------------------------------
#  Challenge Task 1 of 4
#  We have a bunch of prices and sales numbers and
#  we need to find out our total earnings.
#  Let's start by writing a function named
#  product_sales that takes a single two-member
#  tuple made up of a price and a number of units sold.
#  product_sales should return the product of the price
#  and the number of units.
prices = [
    (6.99, 5),
    (2.94, 15),
    (156.99, 2),
    (99.99, 4),
    (1.82, 102)
]

def product_sales(price_unit):
    return price_unit[0] * price_unit[1]

price = (3,5)
print(product_sales(price))

# ------------------------------------------------
#  Challenge Task 2 of 4
#  We need to add two numbers together.
#  We could write a function that does this but that seems silly.
#  Import add from the operator module.
from operator import add

# ------------------------------------------------
#  Challenge Task 3 of 4
#  Alright, one more import. Import reduce() from functools.
from functools import reduce

# ------------------------------------------------
#  Challenge Task 4 of 4
#  Finally, we're ready to find our totals.
#  Create a variable named total.
#  Use map() to find the per-product totals for each item
#  in prices, then use reduce (and add) to find the total value.
total = reduce(add, map(product_sales, prices))
print(total)
