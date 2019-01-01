#
#  Slice Functions
#  Python Techdegree
#
#  Created by Dulio Denis on 12/8/18.
#  Copyright (c) 2018 ddApps. All rights reserved.
# ------------------------------------------------
#  Slice Function Challenge
#  Create a function named first_4 that returns the first four items from whatever iterable is given to it.
def first_4(iterable):
    return iterable[0:4]

print(first_4("Hello"))

# Make a new function named first_and_last_4. 
# It'll accept a single iterable but, this time, 
# it'll return the first four and last four items as a single value.
def first_and_last_4(iterable):
    return iterable[0:4] + iterable[-4:]

print(first_and_last_4("123456789"))

# Create a new function named odds that returns every item with an odd index 
# in a provided iterable. For example, it would return the items at index 1, 3, and so on.
def odds(iterable):
    counter = 0
    new_list = []
    for item in iterable:
        if (counter % 2) != 0:
            new_list.append(item)
        counter += 1
    return new_list

print(odds("0123456789"))
print(odds(""))

# Make a function named reverse_evens that accepts a single iterable as an argument. 
# Return every item in the iterable with an even index...in reverse.
# For example, with [1, 2, 3, 4, 5] as the input, the function would return [5, 3, 1].
def reverse_evens(iterable):
    counter = 0
    new_list = []
    for item in iterable:
        if (counter % 2) == 0:
            new_list.insert(0, item)
        counter += 1
    return new_list

print(reverse_evens("0123456789"))