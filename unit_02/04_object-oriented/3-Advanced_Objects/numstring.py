#
#  Object-Oriented Python: Advanced Objects
#  Python Techdegree
#
#  Created by Dulio Denis on 12/14/18.
#  Copyright (c) 2018 ddApps. All rights reserved.
# ------------------------------------------------
#  Whether we like it or not, someone, somewhere, 
#  is going to turn an instance of our class into a string. 
#  Or an int. Let's make sure it happens like we want.
class NumString:
    def __init__(self, value):
        self.value = str(value)

    def __str__(self):
        return self.value

    def __int__(self):
        return int(self.value)

    def __float__(self):
        return float(self.value)

five = NumString(5)
print(str(five))
