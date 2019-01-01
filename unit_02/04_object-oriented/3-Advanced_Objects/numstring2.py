#
#  Object-Oriented Python: Advanced Objects
#  Python Techdegree
#
#  Created by Dulio Denis on 12/14/18.
#  Copyright (c) 2018 ddApps. All rights reserved.
# ------------------------------------------------
#  Challenge Task 1 of 2
#  This class should look familiar!
#  I need to you add __mul__ to NumString so we can
#  multiply our number string by a number. 
#  Go ahead and add __rmul__, too.
class NumString:
    def __init__(self, value):
        self.value = str(value)

    def __str__(self):
         return self.value

    def __int__(self):
        return int(self.value)

    def __float__(self):
        return float(self.value)
    
    def __add__(self, other):
        if '.' in self.value:
            return float(self) + other
        return int(self) + other
      
    def __radd__(self, other):
        return self + other
    
    def __iadd__(self, other):
        self.value = self + other
        return self.value
    
    def __mul__(self, other):
        if '.' in self.value:
            return float(self) * other
        return int(self) * other

    def __rmul__(self, other):
        return self * other

# Challenge Task 2 of 2
# Now wrap it up by adding in __imul__,
# which does in-place multiplication. 
# Be sure to update self.value!
    def __imul__(self, other):
        self.value = self * other
        return self.value
