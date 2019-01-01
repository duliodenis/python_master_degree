#
#  Object-Oriented Python: Dice Roller
#  Python Techdegree
#
#  Created by Dulio Denis on 12/21/18.
#  Copyright (c) 2018 ddApps. All rights reserved.
# ------------------------------------------------
#  Challenge 3: RPG Roller
# ------------------------------------------------
#  Challenge Task 1 of 2
#  Create a new class in dice.py named D20 that extends Die. 
#  It should automatically have 20 sides and shouldn't require any arguments to create.
import random

class Die:
    def __init__(self, sides=2):
        if sides < 2:
            raise ValueError("Can't have fewer than two sides")
        self.sides = sides
        self.value = random.randint(1, sides)
        
    def __int__(self):
        return self.value
      
    def __add__(self, other):
        return int(self) + other
    
    def __radd__(self, other):
        return self + other

class D20(Die):
    def __init__(self):
        super().__init__(sides=20)

d20 = D20()
print(d20.value)

# ------------------------------------------------
# Challenge Task 2 of 2
# Now update Hand in hands.py. 
# I'm going to use code similar to Hand.roll(2) and 
# I want to get back an instance of Hand with two D20s rolled in it. 
# I should then be able to call .total on the instance to get the total of the two dice.
# I'll leave the implementation of all of that up to you. I don't care how you do it, I only care that it works.
from dice import D20

class Hand(list):
    def __init__(self, size=0, die_class=D20):
        self.size = size
        super().__init__()
        for _ in range(size):
            self.append(die_class())

    @property
    def total(self):
        return sum(self)

    @classmethod
    def roll(cls, size=2):
        return cls(size)

print("Part 2")
hand = Hand()
print(hand.roll(2))
