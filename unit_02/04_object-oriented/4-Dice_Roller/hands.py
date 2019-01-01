#
#  Object-Oriented Python: Dice Roller
#  Python Techdegree
#
#  Created by Dulio Denis on 12/22/18.
#  Copyright (c) 2018 ddApps. All rights reserved.
# ------------------------------------------------
#  Challenge 5: Capitalism, the Game (3 objectives)
# ------------------------------------------------
#  Challenge Task 1 of 3
#  We're playing a popular board game about snatching
#  up real estate in Atlantic City. I need you finish
#  out the CapitalismHand class. 
#  First off, make sure it always rolls two D6s.
from dice import D6

class Hand(list):
    def __init__(self, size=0, die_class=None, *args, **kwargs):
        if not die_class:
            raise ValueError("You must provide a die class")
        super().__init__()
        
        for _ in range(size):
            self.append(die_class())
        self.sort()
        
    def _by_value(self, value):
        dice = []
        for die in self:
            if die == value:
                dice.append(die)
        return dice


class CapitalismHand(Hand):
    def __init__(self, *args, **kwargs):
        super().__init__(size=2, die_class=D6, *args, **kwargs)

    @property
    def ones(self):
        return self._by_value(1)
    
    @property
    def twos(self):
        return self._by_value(2)
    
    @property
    def threes(self):
        return self._by_value(3)
    
    @property
    def fours(self):
        return self._by_value(4)
    
    @property
    def fives(self):
        return self._by_value(5)
    
    @property
    def sixes(self):
        return self._by_value(6)
    
    @property
    def _sets(self):
        return {
            1: len(self.ones),
            2: len(self.twos),
            3: len(self.threes),
            4: len(self.fours),
            5: len(self.fives),
            6: len(self.sixes)
        }
    
# ------------------------------------------------
# Challenge Task 2 of 3
# Alright! Now I need you to add a new property called doubles. 
# It should return True if both of the dice have the same value. 
# Otherwise, return False.

    @property
    def doubles(self):
        return self[0] == self[1]

#  Challenge Task 3 of 3
#  And, finally, if I have doubles, I want to reroll the hand. 
#  Add a classmethod to CapitalismHand named reroll that returns 
#  a new instance of the class, effectively rerolling the hand.

    @classmethod
    def reroll(self):
        return CapitalismHand()