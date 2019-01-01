#
#  Object-Oriented Python: Advanced Objects
#  Python Techdegree
#
#  Created by Dulio Denis on 12/16/18.
#  Copyright (c) 2018 ddApps. All rights reserved.
# ------------------------------------------------
#  Challenge Task 1 of 2
#  Add a new property to the Rectangle class named area. 
#  It should calculate and return the area of the Rectangle 
#  instance (width * length).
# ------------------------------------------------
class Rectangle:
    def __init__(self, width, length):
        self.width = width
        self.length = length

    @property
    def area(self):
        return self.width * self.length

    @property
    def perimeter(self):
        return (self.length * 2) + (self.width * 2) 

r = Rectangle(5, 10)
print(r.area)
print(r.perimeter)

#  Challenge Task 2 of 2
#  Let's add one more property to our Rectangle class. 
#  This time, add a perimeter property that returns the 
#  perimeter of the rectangle (length * 2 + width * 2).

