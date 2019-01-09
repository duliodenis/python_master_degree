#
#  Python Testing: Be Assertive 
#  Python Techdegree
#
#  Created by Dulio Denis on 1/8/19.
#  Copyright (c) 2019 ddApps. All rights reserved.
# ------------------------------------------------
#  Challenge 1: assertTrue and assertFalse
# ------------------------------------------------
#  Challenge Task 1 of 2
#  We haven't used assertTrue yet but I'm sure you
#  can handle this. assertTrue checks that a value
#  is truthy. Complete the first test using 
#  assertTrue. 
#  Provide your own good palindrome or use "tacocat".
# ------------------------------------------------
import unittest

from string_fun import is_palindrome


class PalindromeTestCase(unittest.TestCase):
    def test_good_palindrome(self):
        self.assertTrue(is_palindrome("tacocat"))

# ------------------------------------------------
#  Challenge Task 2 of 2
#  Great! Now let's use the reverse of assertTrue which
#  is assertFalse. Fill out test_bad_palindrome with the
#  assertFalse assertion and a bad palindrome.

    def test_bad_palindrome(self):
        self.assertFalse(is_palindrome("not_palindrome"))
