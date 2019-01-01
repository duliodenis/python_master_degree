#
#  Object-Oriented Python: Dice Roller
#  Python Techdegree
#
#  Created by Dulio Denis on 12/22/18.
#  Copyright (c) 2018 ddApps. All rights reserved.
# ------------------------------------------------
#  Challenge 4: Chance Scoring
# ------------------------------------------------
#  Challenge Task 1 of 2
#  I've set you up with all of the code you've seen
#  in the course. I want you to add a score_chance
#  method to the YatzyScoresheet. 
#  It should take a hand argument. 
#  Return the sum total of the dice in the hand. 
#  For example, a Hand of [1, 2, 2, 3, 4] would return a score of 12.
class YatzyScoresheet:
    def score_ones(self, hand):
        return sum(hand.ones)
    
    def _score_set(self, hand, set_size):
        scores = [0]
        for worth, count in hand._sets.items():
            if count == set_size:
                scores.append(worth*set_size)
        return max(scores)
    
    def score_one_pair(self, hand):
        return self._score_set(hand, 2)

    def score_chance(self, hand):
        score = 0
        for value in hand:
            score += value
        return score

# ------------------------------------------------
# Challenge Task 2 of 2
# Great! Let's make one more scoring method! 
# Create a score_yatzy method. 
# If there are five dice with the same value, return 50. Otherwise, return 0.

    def score_yatzy(self, hand):
        # If the function self._score_set(hand,5) returns True 
        # or any sort of Truthy data it means there are 5 of the same in the hand
        # therefore the if conditions returns 50. 
        if self._score_set(hand, 5):
            return 50
        # else return 0
        else:
            return 0

