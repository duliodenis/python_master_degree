#
#  String Cases Challenge
#  Python Techdegree
#
#  Created by Dulio Denis on 12/10/18.
#  Copyright (c) 2018 ddApps. All rights reserved.
# ------------------------------------------------
# Create a function named stringcases that takes a single string but returns 
# a tuple of different string formats. The formats should be:
#
#    All uppercase
#    All lowercase
#    Titlecased (first letter of each word is capitalized)
#    Reversed
#
# There are str methods for all but the last one.
def stringcases(string):
    all_upper = string.upper()
    all_lower = string.lower()
    title_cased = string.title()
    reversed = "".split(string)

    for letter in string:
        reversed.insert(0, letter)

    return (all_upper, all_lower, title_cased, "".join(reversed))

print(stringcases("Hello World"))