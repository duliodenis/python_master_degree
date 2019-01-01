#
#  Object-Oriented Python: Characters & Students
#  Python Techdegree
#
#  Created by Dulio Denis on 12/13/18.
#  Copyright (c) 2018 ddApps. All rights reserved.
# ------------------------------------------------
#  With vocabulary out of the way, let's see how to define our own classes.
import random

class Thief:
    sneaky = True

    def pickpocket(self):
        print("Called by {}".format(self))
        if self.sneaky:
            return bool(random.randint(0, 1))
        else:
            return False

kenneth = Thief()
print(kenneth.sneaky)
kenneth.sneaky = False
print(kenneth.pickpocket())

Thief.pickpocket(kenneth)

# Challenge Task 1 of 2
# Alright, it's time create your first class all on your own!
# Make a new class named Student. 
# Give it an attribute name and put your own name, as a string, into the attribute.

class Student0:
    name = "Dulio"

# Challenge Task 2 of 2
# Great work!
# Now, make an instance of your class named me.
# Then print() out the name attribute of your instance.

me_zero = Student0()
print(me_zero.name)

# Challenge Task 1 of 1
# This class should look familiar!
# I need you to add a method name praise. 
# The method should return a positive message about the student which includes the name attribute. 
# As an example, it could say "You're doing a great job, Jacinta!" or "I really like your hair today, Michael!".
# Feel free to change the name attribute to your own name, too!

class Student:
    name = "Dulio"

    def praise(self):
        response = "You're doing a great job {}!".format(self.name)
        return response

me = Student()
print(me.praise)

# Challenge Task 1 of 1
# Alright, I need you make a new method named feedback. 
# It should take an argument named grade. 
# Methods take arguments just like functions do. 
# You'll still need self in there, though.
# 
# If grade is above 50, return the result of the praise method. 
# If it's 50 or below, return the reassurance method's result.

    def reassurance(self):
        return "Chin up, {}. You'll get it next time!".format(self.name)

    def feedback(self, grade):
        if grade > 50:
            return self.praise()
        elif grade <= 50:
            return self.reassurance()

    def __init__(self, name, sneaky=True, *kwargs):
        self.name = name
        self.sneaky = sneaky

# Challenge Task 1 of 2
# Our Student class is coming along nicely!
# I'd like to be able to set the name attribute at the same time that I create an instance. 
# Can you add the code for doing that? Remember, you'll need to override the __init__ method.
    def __init__(self, name):
        self.name = name

# Challenge Task 2 of 2
# Great!
# Sometimes I have other attributes I need to store on a Student instance, though. 
# Can you use **kwargs and setattr to add attributes for any other key/value pairs I want to send to the instance when I create it?
    def __init__(self, **kwargs):
        for attribute, value in kwargs.items():
            setattr(self, attribute, value)
