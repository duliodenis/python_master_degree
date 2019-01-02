#
#  Using Databases in Python: Meet Peewee
#  Python Techdegree
#
#  Created by Dulio Denis on 1/1/19.
#  Copyright (c) 2019 ddApps. All rights reserved.
# ------------------------------------------------
#  Now that we have a model, we need to be able to
#  put information into it and then get that 
#  information back out. That's where queries come in.
# ------------------------------------------------
from peewee import *

db = SqliteDatabase('students2.db')

class Student(Model):
    username = CharField(max_length=255, unique=True)
    points = IntegerField(default=0)

    class Meta:
        database = db


students = [
    {'username': 'kennethlove', 'points': 4888},
    {'username': 'jerryseinfeld', 'points': 11912},
    {'username': 'elainebenice', 'points': 7363},
    {'username': 'cosmokramer', 'points': 4079},
]

def add_students():
    for student in students:
        try:
            Student.create(username = student['username'],
                           points=student['points'])
        except IntegrityError:
            student_record = Student.get(username=student['username'])
            student_record.points = student['points']
            student_record.save()

def top_student():
    student = Student.select().order_by(Student.points.desc()).get()
    return student

if __name__ == '__main__':
    db.connect()
    db.create_tables([Student], safe=True)
    add_students()
    print("Our top student is {0.username}.".format(top_student()))
