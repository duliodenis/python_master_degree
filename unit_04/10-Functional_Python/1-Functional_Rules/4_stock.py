#
#  Functional Python: What We're Going to Work With
#  Python Techdegree
#
#  Created by Dulio Denis on 2/25/19.
#  Copyright (c) 2019 ddApps. All rights reserved.
# ------------------------------------------------
#  Let's get to some code!
#  We'll look at our data, our datatypes that we'll
#  be using, and talk about what functions as
#  first-class citizens gets us.
import json


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