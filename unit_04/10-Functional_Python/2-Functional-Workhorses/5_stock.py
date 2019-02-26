#
#  Functional Python: Functional Workhorses
#  Python Techdegree
#
#  Created by Dulio Denis on 2/26/19.
#  Copyright (c) 2019 ddApps. All rights reserved.
# ------------------------------------------------
#  More than just a friend of Dora or a way to find
#  things, `map()` lets us apply transformations to
#  each item in an iterable.
import json
from operator import attrgetter, itemgetter
from copy import copy

class Book:
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

    def __str__(self):
        return self.title
    
    def __repr__(self):
        return str(self)
    
    
def get_books(filename, raw=False):
    try:
        data = json.load(open(filename))
    except FileNotFoundError:
        return []
    else:
        if raw:
            return data['books']
        return [Book(**book) for book in data['books']]
    
BOOKS = get_books('books.json')
RAW_BOOKS = get_books('books.json', raw=True)

def sales_price(book):
    """Apply a 20% discount to the book price."""
    book = copy(book)
    book.price = round(book.price-book.price*.2, 2)
    return book

sales_books = list(map(sales_price, BOOKS))
print(sales_books)
