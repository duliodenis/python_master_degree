#
#  Object-Oriented Python: Dice Roller
#  Python Techdegree
#
#  Created by Dulio Denis on 12/22/18.
#  Copyright (c) 2018 ddApps. All rights reserved.
# ------------------------------------------------
#  Score Sheets
#  Now that we have a handful of dice, we should 
#  build the logic for scoring them while we play 
#  the game.
# ------------------------------------------------
from hands import YatzyHand
from dice import D6

class YatzyScoresheet:
    def score_ones(self, hand):
        return sum(hand.ones)

    def score_twos(self, hand):
        return sum(hand.twos)

    def score_threes(self, hand):
        return sum(hand.threes)

    def score_fours(self, hand):
        return sum(hand.fours)

    def score_fives(self, hand):
        return sum(hand.fives)

    def score_sixes(self, hand):
        return sum(hand.sixes)

    def _score_set(self, hand, set_size):
        scores = [0]
        for worth, count in hand._sets.items():
            if count == set_size:
                scores.append(worth * set_size)
        return max(scores)

    def score_one_pair(self, hand):
        return self._score_set(hand, 2)

    def score_chance(self, hand):
        score = 0
        for value in hand:
            score += value
        return score

    def score_yatzy(self, hand):
        # If the function self._score_set(hand,5) returns True 
        # or any sort of Truthy data it means there are 5 of the same in the hand
        # therefore the if conditions returns 50. 
        if self._score_set(hand, 5):
            return 50
        # else return 0
        else:
            return 0



# TEST
# -------------------------
print("Score Sheet Testing")
hand = YatzyHand()
three = D6(value=3)
four  = D6(value=4)
one   = D6(value=1)
two   = D6(value=2)
hand[:] = [one, three, three, four, four]
print(hand)
print(YatzyScoresheet().score_one_pair(hand))

hand[:] = [one, two, two, three, four]
print(YatzyScoresheet().score_chance(hand))

print("Score Test")
print(YatzyScoresheet().score_yatzy(hand))
hand[:] = [one, one, one, one, one]
print(YatzyScoresheet().score_yatzy(hand))
