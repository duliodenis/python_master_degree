#
#  Python Testing: First Steps with Testing 
#  Python Techdegree
#
#  Created by Dulio Denis on 1/6/19.
#  Copyright (c) 2019 ddApps. All rights reserved.
# ------------------------------------------------
#  Challenge 2: Simple Unit Test
# ------------------------------------------------
#  Challenge Task 1 of 2
#  Import the unittest module.
import unittest

# ------------------------------------------------
#  Challenge Task 2 of 2
#  Create a TestCase named SimpleTestCase with a
#  simple test that asserts that 10 - 10 is 0. 
#  Remember, unittest test names have to start with test_.
class SimpleTestCase(unittest.TestCase):
    def test_simple_test(self):
        assert 10 - 10 == 0

if __name__ == "__main__":
    unittest.main()
