#
#  Object-Oriented Python: Advanced Objects
#  Python Techdegree
#
#  Created by Dulio Denis on 12/16/18.
#  Copyright (c) 2018 ddApps. All rights reserved.
# ------------------------------------------------
#  We haven't talked about access control yet. 
# ------------------------------------------------
class Protected:
    __name = "Security"

    def __method(self):
        return self.__name

p = Protected()
# these do not work
# p.__name
# p.__method()

# but with name mangling it does
print(p._Protected__name)

class Circle:
    def __init__(self, diameter):
        self.diameter = diameter

    @property
    def radius(self):
        return self.diameter / 2

    @radius.setter
    def radius(self, radius):
        self.diameter = radius * 2

c = Circle(10)
print(c.diameter)
print(c.radius)
c.radius = 20
print(c.diameter)
