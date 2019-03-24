#
#  Data Structures: Linked List Merge Sort: The Divide Step
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

def split(linked_list):
    '''
    Divide the unsorted list at the midpoint into sublists.
    '''
    if linked_list == None or linked_list.head == None:
        left_half = linked_list
        right_half = None
        return left_half, right_half
    else: # non-empty linked lists
        size = linked_list.len()
        midpoint = size // 2
        mid_node = linked_list.node_at_index(midpoint-1)

        left_half = linked_list
        right_half = LinkedList()
        right_half = mid_node.next_node
        mid_node.next_node = None
        return left_half, right_half
    