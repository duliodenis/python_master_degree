#
#  Algorithms: Algorithms in Code (Recursive Binary Search)
#  Python Techdegree
#
#  Created by Dulio Denis on 3/23/19.
#  Copyright (c) 2019 ddApps. All rights reserved.
# ------------------------------------------------
#  NOTE: Python has a maximum recursion depth and
#        an iterative approach is still preferred
#
def recursive_binary_search(list, target):
    '''
    Returns the index position of the target if found, else returns None
    '''
    if len(list) == 0:
        return False
    midpoint = len(list) // 2
    if list[midpoint] == target:
        return True
    if list[midpoint] < target:
        return recursive_binary_search(list[midpoint+1:], target)
    else:
        return recursive_binary_search(list[:midpoint], target)
    
list = [1, 2, 3, 4, 5, 6]
print(recursive_binary_search(list, 3))
print(recursive_binary_search(list, 7))

def recursive_binary_search_2(list, target, start=0, end=None):
    '''
    The function has been modified to accept a start and end position
    with default values of 0 and None respectively. 
    The default values allow us to pass a list and target without needing
    to specify the arguments when invoking the function.
    Inside the body we set the appropriate values like we did when setting
    first and last in the iterative approach. 
    '''
    if end is None:
        end = len(list) - 1
    if start > end:
        return None

    midpoint = (start + end) // 2

    if target == list[midpoint]:
        return midpoint
    else:
        if target < list[midpoint]:
            return recursive_binary_search_2(list, target, start, midpoint-1)
        else:
            return recursive_binary_search_2(list, target, midpoint+1, end)

list = [1, 2, 3, 4, 5, 6]
print(recursive_binary_search_2(list, 3))
print(recursive_binary_search_2(list, 7))
