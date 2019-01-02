#
#  Using Databases in Python: Meet Peewee
#  Python Techdegree
#
#  Created by Dulio Denis on 12/31/18.
#  Copyright (c) 2018 ddApps. All rights reserved.
# ------------------------------------------------
#  What good is a database without tables? 
#  Let's build a model, connect to our database, 
#  and turn our model into a table.
# ------------------------------------------------
from peewee import *

db = SqliteDatabase('students.db')

class Student(Model):
    username = CharField(max_length=255, unique=True)
    points = IntegerField(default=0)

    class Meta:
        database = db

if __name__ == '__main__':
    db.connect()
    db.create_tables([Student], safe=True)
