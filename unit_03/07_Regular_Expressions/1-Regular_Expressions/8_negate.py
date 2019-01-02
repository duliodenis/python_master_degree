#
#  Regular Expressions in Python
#  Python Techdegree
#
#  Created by Dulio Denis on 12/29/18.
#  Copyright (c) 2018 ddApps. All rights reserved.
# ------------------------------------------------
#  Challenge 6: Negated Numbers
# ------------------------------------------------
#  Challenge Task 1 of 1
#  Create a variable named good_numbers that is an
#  re.findall() where the pattern matches anything
#  in string except the numbers 5, 6, and 7.
import re

string = '1234567890'

good_numbers = re.findall(r'[^567]', string)

print(good_numbers)
