#
#  Object-Oriented Python: Dice Roller
#  Python Techdegree
#
#  Created by Dulio Denis on 12/17/18.
#  Copyright (c) 2018 ddApps. All rights reserved.
# ------------------------------------------------
#  Final Project for Object Oriented Python Course
#  With all of our object-oriented programming knowledge, 
#  it's time to tackle a bigger, more comprehensive project.
# ------------------------------------------------
import random

class Die:
    def __init__(self, sides=2, value=0):
        if not sides >= 2:
            raise ValueError("A die must have AT LEAST two sides.")
        if not isinstance(sides, int):
            raise ValueError("Sides must be whole numbers.")
        self.value = value or random.randint(1, sides)

    def __int__(self):
        return int(self.value)

    def __eq__(self, other):
        return int(self) == other

    def __ne__(self, other):
        return not int(self) == other

    def __gt__(self, other):
        return int(self) > other

    def __lt__(self, other):
        return int(self) < other

    def __ge__(self, other):
        return int(self) > other or int(self) == other

    def __le__(self, other):
        return int(self) < other or int(self) == other

    def __add__(self, other):
        return int(self) + other
    
    def __radd__(self, other):
        return int(self) + other

    def __repr__(self):
        return str(self.value)

class D6(Die):
    def __init__(self, value=0):
        super().__init__(sides=6, value=value)


# TESTS
print("Master Object >-----------")
d = Die()
print(d.value)

print("EQUALITY CHECK >-----------")

dice1 = D6()
print(dice1.value)

dice2 = D6()
print(dice2.value)

if dice1 == dice2:
    print("The dice are equal")
else:
    print("The dice are not equal")

print("\nGreater than or less than -----")

if dice1 > dice2:
    print("d6 is greater than d6B")
elif dice1 < dice2:
    print("d6 is less than d6B")
else:
    print("The die are neither greater than or less than - they must be equal")

print("--------------------------")

print("The two dice add up to: {}".format(dice1 + dice2))

print("--------------------------")
