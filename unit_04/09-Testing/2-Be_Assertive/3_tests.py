#
#  Python Testing: Be Assertive 
#  Python Techdegree
#
#  Created by Dulio Denis on 1/9/19.
#  Copyright (c) 2019 ddApps. All rights reserved.
# ------------------------------------------------
#  The `unittest` library has many different
#  assertions but some are more commonly used than
#  others. Let's look at how to check for membership,
#  what class a variable is an instance of, and a
#  couple of others.
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
