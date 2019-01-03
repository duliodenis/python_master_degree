#
#  Using Databases in Python: Diary App
#  Python Techdegree
#
#  Created by Dulio Denis on 1/3/19.
#  Copyright (c) 2019 ddApps. All rights reserved.
# ------------------------------------------------
#  Let's define our model and get our database
#  connection set up. We'll also make our script
#  executable so we can run it in a nicer manner.
# ------------------------------------------------
#!/usr/bin/env python3

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

def add_entry():
    '''Add an entry.'''

def view_entries():
    '''View previous entries.'''

def delete_entry():
    '''Delete an entry.'''

if __name__ == "__main__":
    initialize()
    menu_loop()
