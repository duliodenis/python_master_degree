#
#  Python Testing: Be Assertive 
#  Python Techdegree
#
#  Created by Dulio Denis on 1/7/19.
#  Copyright (c) 2019 ddApps. All rights reserved.
# ------------------------------------------------
#  A lot of the assertions you'll write in your
#  tests have to do with values. You'll want to
#  assert that something is bigger than 5 or has
#  less than 3 items. Let's look at the assertions
#  provided for comparing against numbers.
# ------------------------------------------------
import unittest

import moves

class MoveTests(unittest.TestCase):
    def setUp(self):
        self.rock = moves.Rock()
        self.paper = moves.Paper()
        self.scissors = moves.Scissors()

    def test_five_plus_five(self):
        assert 5 + 5 == 10

    def test_one_plus_one(self):
        assert not 1 + 1 == 3

    def test_equal(self):
        self.assertEqual(self.rock, moves.Rock())

    def test_not_equal(self):
        self.assertNotEqual(self.rock, self.paper)

    def test_rock_better_than_scissors(self):
        self.assertGreater(self.rock, self.scissors)

    def test_paper_worse_than_scissors(self):
        self.assertLess(self.paper, self.scissors)

# run it all the time
if __name__ == "__main__":
    unittest.main()