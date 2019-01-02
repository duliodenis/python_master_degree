#
#  Regular Expressions in Python
#  Python Techdegree
#
#  Created by Dulio Denis on 12/28/18.
#  Copyright (c) 2018 ddApps. All rights reserved.
# ------------------------------------------------
#  Challenge 3: Phone Numbers
# ------------------------------------------------
#  Challenge Task 1 of 1
#  Create a function named phone_numbers that takes
#  a string and returns all of the phone numbers in
#  the string using re.findall(). The phone numbers
#  will all be in the format 555-555-5555.
import re

def phone_numbers(data):
    return re.findall(r'\d{3}-\d{3}-\d{4}', data)

print(phone_numbers("hello 212-820-5357 there 1234"))
