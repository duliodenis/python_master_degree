#
#  Object-Oriented Python: Advanced Objects
#  Python Techdegree
#
#  Created by Dulio Denis on 12/15/18.
#  Copyright (c) 2018 ddApps. All rights reserved.
# ------------------------------------------------
#  Subclassing Built-ins Challenge (Lists)
# ------------------------------------------------
# Challenge Task 1 of 1
# Now I want you to make a subclass of list. Name it Liar.
# Override the __len__ method so that it always returns 
# the wrong number of items in the list. 
# For example, if a list has 5 members, the Liar class 
# might say it has 8 or 2.
# You'll probably need super() for this.
class Liar(list):
    def __len__(self):
        return 2

# Another solution using super
class Liar(list):
    def __len__(self):
        return super().__len__() + 2
