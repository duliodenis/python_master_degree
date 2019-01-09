#
#  Python Testing: Be Assertive 
#  Python Techdegree
#
#  Created by Dulio Denis on 1/8/19.
#  Copyright (c) 2019 ddApps. All rights reserved.
# ------------------------------------------------
#  The `unittest` library has many different
#  assertions but some are more commonly used than
#  others. Let's look at how to check for membership,
#  what class a variable is an instance of, and a
#  couple of others.
# ------------------------------------------------
import unittest

import dice

class DieTest(unittest.TestCase):
    def setUp(self):
        self.d6 = Die(6)
        self.d8 = Die(8)

    def test_creation(self):
        self.assertEqual(self.d6.sides, 6)
        