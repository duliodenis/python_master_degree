#
#  Functional Python: Functional Workhorses (Filter)
#  Python Techdegree
#
#  Created by Dulio Denis on 3/2/19.
#  Copyright (c) 2019 ddApps. All rights reserved.
# ------------------------------------------------
#  Filters are a very useful utility in programming,
#  letting you refine a group of items into just
#  the ones that meet your criteria.
#  It's a "must be this tall to ride" sign for your data!
"""
   filter() takes a function and an iterable. The function, 
   like with map(), takes only a single argument and is applied
   to each item in the iterable. If the function returns a truthy
   value for the item, the item is sent back to filter() which,
   ultimately, returns a new iterable of the filtered items.
   
   You can achieve the same effect with 
   [item for item in iterable if func(item)]. 
   Again, like with map(), this can be more quickly readable for small applications.
   
   I mentioned filterfalse(). 
   This function works just like filter() but only returns 
   things where the filter function gives back a False or 
   non-truthy value. You can read more in the documentation.
   https://docs.python.org/3/library/itertools.html#itertools.filterfalse
"""
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

def is_long_book(book):
    """Does a book have 600+ pages?"""
    return book.number_of_pages >= 600

long_book = list(filter(is_long_book, BOOKS))
long_book_comprehension_with_function = [book for book in BOOKS if is_long_book(book)]
log_book_comprehension = [book for book in BOOKS if book.number_of_pages >= 600]

print("Of the {} books, {} of them are long".format(len(BOOKS), len(long_book)))
print(len(log_book_comprehension))
print(len(long_book_comprehension_with_function))
