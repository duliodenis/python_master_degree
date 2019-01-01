#
#  Combo Challenge Task
#  Python Techdegree
#
#  Created by Dulio Denis on 12/10/18.
#  Copyright (c) 2018 ddApps. All rights reserved.
# ------------------------------------------------
#  Alright, this one can be tricky but I'm sure you can do it.
#  Create a function named combo that takes two ordered iterables. 
#  These could be tuples, lists, strings, whatever.
#  Your function should return a list of tuples. 
#  Each tuple should hold the first item in each iterable, 
#  then the second set, then the third, and so on. 
#  Assume the iterables will be the same length.
#  Example:
#   combo([1, 2, 3], 'abc')
#   Output:
#   [(1, 'a'), (2, 'b'), (3, 'c')]
def combo(iterable1, iterable2):
    response = []
    length = len(iterable1)
    for i in range(length):
        response += [(iterable1[i], iterable2[i])]
    return response

print(combo([1, 2, 3], 'abc'))