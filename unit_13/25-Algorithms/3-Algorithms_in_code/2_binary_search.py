#
#  Algorithms: Algorithms in Code (Binary Search)
#  Python Techdegree
#
#  Created by Dulio Denis on 3/23/19.
#  Copyright (c) 2019 ddApps. All rights reserved.
# ------------------------------------------------
def binary_search(list, target):
    '''
    Returns the index position of the target if found, else returns None
    '''
    first_position = 0
    last_position = len(list) -1

    while first_position <= last_position:
        midpoint = (first_position + last_position) // 2

        if list[midpoint] == target:
            return midpoint
        elif list[midpoint] < target:
            first_position = midpoint + 1
        else:
            last_position = midpoint - 1
        
    return None

list = [1, 2, 3, 4, 5, 6]
print(binary_search(list, 3))
print(binary_search(list, 7))
