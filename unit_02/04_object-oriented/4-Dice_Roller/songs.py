#
#  Object-Oriented Python: Dice Roller
#  Python Techdegree
#
#  Created by Dulio Denis on 12/19/18.
#  Copyright (c) 2018 ddApps. All rights reserved.
# ------------------------------------------------
#  Challenge 2: Songs
# ------------------------------------------------
#  Challenge Task 1 of 1
#  I'd like to compare songs by their length 
#  (measured in whole seconds). Add the required 
#  methods for ==, <, >, <=, and >= comparisons. 
#  Probably a good idea to be able to convert Songs to ints, too, huh?
class Song:
    def __init__(self, artist, title, length):
        self.artist = artist
        self.title = title
        self.length = length

    def __int__(self):
        return int(self.length)

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

