#
#  Object-Oriented Python: Advanced Objects
#  Python Techdegree
#
#  Created by Dulio Denis on 12/16/18.
#  Copyright (c) 2018 ddApps. All rights reserved.
# ------------------------------------------------
#  Constructicons
#  What if we need something more complex than just 
#  a custom init or new method?
# ------------------------------------------------
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return "{} by {}".format(self.title, self.author)

class Bookcase:
    def __init__(self, books=None):
        self.books = books

    @classmethod
    def create_bookcase(cls, book_list):
        books = []
        for title, author in book_list:
            books.append(Book(title, author))
        return cls(books)

bc = Bookcase.create_bookcase([('Moby Dick', 'Herman Melville'), ('Wuthering Heights', 'Emily Bronte')])
print(str(bc.books[0]))