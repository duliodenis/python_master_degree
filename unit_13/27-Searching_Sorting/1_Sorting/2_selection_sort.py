#
#  Algorithms: Sorting and Searching: Selection Sort
#  Python Techdegree
#
#  Created by Dulio Denis on 3/25/19.
#  Copyright (c) 2019 ddApps. All rights reserved.
# ------------------------------------------------
import sys
from load import load_numbers

numbers = load_numbers(sys.argv[1])
# ------------------------------------------------
def selection_sort(values):
    # We'll create an empty list that will hold all our sorted values.
    sorted_list = []
    print("%-25s %-25s" % (values, sorted_list))

    # We'll loop once for each value in the list.
    for i in range(0, len(values)):
        # We call a function named index_of_min that find the minimum 
        # value in the unsorted list and return its index.
        index_to_move = index_of_min(values)

        # Then we call the "pop" method on the list, and pass it the
        # index of the minimum value. pop will remove that item from the
        # list and return it. We then add that value at the end of the
        # sorted list.
        sorted_list.append(values.pop(index_to_move))
        print("%-25s %-25s" % (values, sorted_list))
    # After the loop finishes, we return the sorted list.
    return sorted_list

def index_of_min(values):
    '''
    Picks out the minimum value. We pass in the list we're going to search.
    '''
    # We mark the first value in the list as the minimum. 
    min_index = 0

    # Now we loop through the remaining values in the list after the first.
    for i in range(1, len(values)):
        # We test whether the value we're currently looking at is less than
        # the previously recorded minimum.
        if values[i] < values[min_index]:
            # If it is, then we set the current index as the new index of
            # the minimum value.
            min_index = i
    # After we've looped through all the values, we return the index of
    # the smallest value we found.
    return min_index

sorted_numbers = selection_sort(numbers)
print(sorted_numbers)