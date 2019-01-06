#
#  Using Databases in Python: Gettin' CRUD-y With It 
#  Python Techdegree
#
#  Created by Dulio Denis on 1/5/19.
#  Copyright (c) 2019 ddApps. All rights reserved.
# ------------------------------------------------
#  If we're going to have a diary, we have to be
#  able to add entries to it. Let's use sys.stdin
#  so we can capture new lines and tabs and all
#  sorts of other goodies.
# ------------------------------------------------
#!/usr/bin/env python3
from collections import OrderedDict
import datetime
import sys

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
    print("Enter your entry. Press 'cntl-d' when finished." )
    data = sys.stdin.read().strip()

    if data:
        if input('Save entry? [Yn]').lower() != 'n':
            Entry.create(content=data)
            print("Saved successfully.")

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
 