#
#  Regular Expressions in Python
#  Python Techdegree
#
#  Created by Dulio Denis on 12/28/18.
#  Copyright (c) 2018 ddApps. All rights reserved.
# ------------------------------------------------
#  Challenge 2: Escapes
# ------------------------------------------------
#  Challenge Task 1 of 2
#  Write a function named first_number that takes
#  a string as an argument. The function should
#  search, with a regular expression, the first
#  number in the string and return the match object.
import re

def first_number(data):
    return re.search(r'\d', data)

print(first_number("Hello5there"))

# ------------------------------------------------
# Challenge Task 2 of 2
# Now, write a function named numbers() that takes 
# two arguments: a count as an integer and a string. 
# Return an re.search for exactly count numbers in 
# the string. 
# Remember, you can multiply strings and integers to 
# create your pattern.
# For example: r"\w" * 5 would create r"\w\w\w\w\w".
def numbers(count, data):
    pattern = r"\d"*count
    return re.search(pattern, data)

print(numbers(2, "hello12there134"))
