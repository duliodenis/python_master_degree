#
#  Using Databases in Python: Diary App
#  Python Techdegree
#
#  Created by Dulio Denis on 1/2/19.
#  Copyright (c) 2019 ddApps. All rights reserved.
# ------------------------------------------------
#  We should nail down what we want our app to do. 
#  Let's stub out most of it with comments.
# ------------------------------------------------
from peewee import *

db = SqliteDatabase('diary.db')

class Entry(Model):
    # content
    # timestamp

    class Meta:
        database = db
    
def menu_loop():
    '''Add an entry.'''

def add_entry():
    '''Add an entry.'''

def view_entries():
    '''View previous entries.'''

def delete_entry():
    '''Delete an entry.'''

if __name__ == "__main__":
    menu_loop()
