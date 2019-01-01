#
#  Random Library
#  Python Techdegree
#
#  Created by Dulio Denis on 12/12/18.
#  Copyright (c) 2018 ddApps. All rights reserved.
# ------------------------------------------------
#  Challenge Task 1 of 1
#  I haven't shown you how to use this function yet but I'm sure you can use it. 
#  In the random library, there's a function named sample that takes two arguments: 
#  an iterable to sample from, and an integer of how many unique samples to return.
#  Finish the get_locations function so that it returns 3 unique values from the cells argument.
import random

CELLS = [(0,0), (1,0), (2,0), (3,0), (4,0),
         (0,1), (1,1), (2,1), (3,1), (4,1),
         (0,2), (1,2), (2,2), (3,2), (4,2),
         (0,3), (1,3), (2,3), (3,3), (4,3),
         (0,4), (1,4), (2,4), (3,4), (4,4)]

def get_locations(cells):
    values = random.sample(cells, 3)
    return values

print(get_locations(CELLS))