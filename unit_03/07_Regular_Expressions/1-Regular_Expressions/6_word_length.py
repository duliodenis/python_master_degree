#
#  Regular Expressions in Python
#  Python Techdegree
#
#  Created by Dulio Denis on 12/29/18.
#  Copyright (c) 2018 ddApps. All rights reserved.
# ------------------------------------------------
#  Challenge 4: Word Length
# ------------------------------------------------
#  Challenge Task 1 of 1
#  Create a function named find_words that takes a
#  count and a string. Return a list of all of the
#  words in the string that are count word characters
#  long or longer.
import re

# EXAMPLE:
# >>> find_words(4, "dog, cat, baby, balloon, me")
# ['baby', 'balloon']

def find_words(count, data):
    return re.findall(r"\w{"+str(count)+",}", data)

# TEST
print(find_words(4, "dog, cat, baby, balloon, me"))
