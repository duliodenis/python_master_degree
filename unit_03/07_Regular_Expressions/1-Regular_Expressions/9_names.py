#
#  Regular Expressions in Python
#  Python Techdegree
#
#  Created by Dulio Denis on 12/29/18.
#  Copyright (c) 2018 ddApps. All rights reserved.
# ------------------------------------------------
#  Challenge 7: Named Groups
# ------------------------------------------------
#  Challenge Task 1 of 1
#  Create a variable names that is an re.match() 
#  against string. The pattern should provide two
#  groups, one for a last name match and one for a
#  first name match. The name parts are separated 
#  by a comma and a space.
import re

string = 'Perotto, Pier Giorgio'

names = re.match(r'''
    ^(?P<last_name>[\w]*),\s    # Last name
     (?P<first_name>[\w\s\w]*)$ #first name
''', string, re.X)

print(names)
