#
#  Python Testing: Be Assertive 
#  Python Techdegree
#
#  Created by Dulio Denis on 1/12/19.
#  Copyright (c) 2019 ddApps. All rights reserved.
# ------------------------------------------------
#  Challenge 3: assertRaises
# ------------------------------------------------
#  Challenge Task 1 of 2
#  Our get_anagrams() function raises a ValueError
#  when you pass it an empty string.
#  Finish the test to make sure this happens.
#  You'll want to use assertRaises.
import unittest

from string_fun_2 import get_anagrams


class AnagramTestCase(unittest.TestCase):
    def test_empty_string(self):
        with self.assertRaises(ValueError):
            get_anagrams("")


# ------------------------------------------------
#  Challenge Task 2 of 2
#  Now add a new test, test_no_args that should
#  also assertRaises(ValueError).
#  This time, call get_anagrams() with no arguments.
    def test_no_args(self):
        with assertRaises(ValueError):
            get_anagrams()
