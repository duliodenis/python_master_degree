#
#  Using Databases in Python: Diary App
#  Python Techdegree
#
#  Created by Dulio Denis on 1/4/19.
#  Copyright (c) 2019 ddApps. All rights reserved.
# ------------------------------------------------
#  We can start to get into the actual behavior of
#  our application now. We'll use an OrderedDict
#  to hold onto our choices and a nifty trick to
#  print out the options to the user and then run
#  their selected function.
# ------------------------------------------------
#!/usr/bin/env python3
from collections import OrderedDict
import datetime

from peewee import *

db = SqliteDatabase('diary.db')

class Entry(Model):
    content = TextField()
    timestamp = DateTimeField(default=datetime.datetime.now) 

    class Meta:
        database = db
    
def initialize():
    '''Create the database and the table if they don't exist.'''
    db.connect()
    db.create_tables([Entry], safe=True)

def menu_loop():
    '''Add an entry.'''
    choice = None

    while choice != 'q':
        print("Enter 'q' to quit.")
        for key, value in menu.items():
            print('{}) {}'.format(key, value.__doc__))
        choice = input('Action: ').lower().strip()

        if choice in menu:
            menu[choice]()

def add_entry():
    '''Add an entry.'''

def view_entries():
    '''View previous entries.'''

def delete_entry():
    '''Delete an entry.'''

menu = OrderedDict([
    ('a', add_entry),
    ('v', view_entries), 
])

if __name__ == "__main__":
    initialize()
    menu_loop()
