#
#  Algorithms: Algorithms in Code (Linear Search)
#  Python Techdegree
#
#  Created by Dulio Denis on 3/23/19.
#  Copyright (c) 2019 ddApps. All rights reserved.
# ------------------------------------------------
def linear_search(list, target):
    '''
    Returns the index position of the target if found, else returns None
    '''
    for i, item in enumerate(list):
        if item == target:
            return i
    return None

list = [1, 2, 3, 4, 5, 6]
print(linear_search(list, 3))
print(linear_search(list, 7))
