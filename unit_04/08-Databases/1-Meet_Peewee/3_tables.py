#
#  Using Databases in Python: Meet Peewee
#  Python Techdegree
#
#  Created by Dulio Denis on 1/1/19.
#  Copyright (c) 2019 ddApps. All rights reserved.
# ------------------------------------------------
#  Challenge 1: Create Table
# ------------------------------------------------
#  Challenge Task 1 of 4
#  Import everything from the peewee library.
from peewee import *

# ------------------------------------------------
#  Challenge Task 2 of 4
#  Now we need to make a database connection. 
#  Make an SqliteDatabase() named "challenges.db". 
#  Assign it to the variable db.
db = SqliteDatabase('challenges.db')

# ------------------------------------------------
#  Challenge Task 3 of 4
#  Alright, now for the biggest part. 
#  Make a model named Challenge that has two fields, 
#  name and language. 
#  Both fields should be of the type CharField with a max_length of 100.
class Challenge(Model):
    name = CharField(max_length=100)
    language = CharField(max_length=100)

# ------------------------------------------------
#  Challenge Task 4 of 4
#  Now add a Meta class to Challenge and set the database attribute equal to db.
    class Meta:
        database = db
