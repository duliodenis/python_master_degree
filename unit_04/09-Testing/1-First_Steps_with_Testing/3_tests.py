#
#  Python Testing: First Steps with Testing 
#  Python Techdegree
#
#  Created by Dulio Denis on 1/6/19.
#  Copyright (c) 2019 ddApps. All rights reserved.
# ------------------------------------------------
#  Most of the power of testing in Python comes
#  from the `unittest` framework and it's `TestCase`
#  class. Let's look at starting a `TestCase` and
#  writing a couple of simple tests.
# ------------------------------------------------
#  Run with: python3 -m unittest 3_tests.py
import unittest

import moves

class MoveTests(unittest.TestCase):
    def test_five_plus_five(self):
        assert 5 + 5 == 10

    def test_one_plus_one(self):
        assert not 1 + 1 == 3


# run it all the time
if __name__ == "__main__":
    unittest.main()
