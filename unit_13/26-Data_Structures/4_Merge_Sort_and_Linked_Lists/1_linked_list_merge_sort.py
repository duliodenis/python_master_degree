#
#  Data Structures: Linked List Merge Sort
#  Python Techdegree
#
#  Created by Dulio Denis on 3/24/19.
#  Copyright (c) 2019 ddApps. All rights reserved.
# ------------------------------------------------
from linked_list import Node, LinkedList

def merge_sort(linked_list):
    '''
    Sorts a linked list in ascending order.
    - Recuresively divide the linked list into sublists containing a single node
    - Repeatedly merge the sublists to produce sorted swublists until one remains
    Returns a sorted linked list.
    '''
    if linked_list.len() == 1:
        return linked_list
    elif linked_list.is_empty():
        return linked_list
    
    left_half, right_half = split(linked_list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left, right)
