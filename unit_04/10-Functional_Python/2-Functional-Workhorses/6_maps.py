#
#  Functional Python: Functional Workhorses
#  Python Techdegree
#
#  Created by Dulio Denis on 3/2/19.
#  Copyright (c) 2019 ddApps. All rights reserved.
# ------------------------------------------------
#  Map Challenge
# ------------------------------------------------
#  Challenge Task 1 of 2
#  Create a function named reverse that takes a
#  single iterable item and returns a reversed
#  version of that item.
backwards = [
    'tac',
    'esuoheerT',
    'htenneK',
    [5, 4, 3, 2, 1],
]

def reverse_list(items):
    return_item = []
    for item in items:
        return_item.insert(0, item)
    return return_item

def reverse(iterable):
    return iterable[::-1]

print(reverse(backwards[0]))
print(reverse(backwards[3]))

# ------------------------------------------------
#  Challenge Task 2 of 2
#  Now use map() to create a variable named forwards.
#  forwards should use reverse() to reverse the order
#  of every item in backwards.
forwards = map(reverse,backwards)

print(list(forwards))
