#
#  Python Testing: Covering Your Bases 
#  Python Techdegree
#
#  Created by Dulio Denis on 1/13/19.
#  Copyright (c) 2019 ddApps. All rights reserved.
# ------------------------------------------------
#  `coverage.py` is an amazing library for
#  determining how much of your code is covered
#  by your tests and how much still needs to be
#  tested. Let's look at how to install it, run it,
#  and get handy reports from it.
#  Aim for 90% coverage.
# ------------------------------------------------
#  Run:
#  pip3 install coverage
#  then:
#  coverage run 1_tests.py
#  coverage report
#  coverage report -m
# ------------------------------------------------
#  Name         Stmts   Miss  Cover   Missing
# ------------------------------------------
# 1_tests.py      34      0   100%
# dice.py         50      9    82%   26, 60, 63, 66, 69, 72-75
# ------------------------------------------
# TOTAL           84      9    89%
# ------------------------------------------------
import unittest

from dice import Die, Roll

class DieTest(unittest.TestCase):
    def setUp(self):
        self.d6 = Die(6)
        self.d8 = Die(8)

    def test_creation(self):
        self.assertEqual(self.d6.sides, 6)
        self.assertIn(self.d6.value, range(1,7))

    def test_add(self):
        self.assertIsInstance(self.d6+self.d8, int)

    def test_bad_sides(self):
        with self.assertRaises(ValueError):
            Die(1)

class RollTest(unittest.TestCase):
    def setUp(self):
        self.hand1 = Roll('1d2')
        self.hand3 = Roll('3d6')

    # test upper and lower boundary on these rolls
    def test_lower(self):
        self.assertGreaterEqual(int(self.hand3), 3)

    def test_upper(self):
        self.assertLessEqual(int(self.hand3), 18)

    def test_membership(self):
        test_die = Die(2)
        test_die.value = self.hand1.results[0].value
        self.assertIn(test_die, self.hand1.results)

    def test_bad_description(self):
        with self.assertRaises(ValueError):
            Roll('2b6')

    def test_small_die(self):
        with self.assertRaises(ValueError):
            Roll('1d2') # totally acceptable - won't fail

    def test_adding(self):
        self. assertEqual(self.hand1+self.hand3,
                          sum(self.hand1.results)+sum(self.hand3.results))

if __name__ == '__main__':
    unittest.main()
