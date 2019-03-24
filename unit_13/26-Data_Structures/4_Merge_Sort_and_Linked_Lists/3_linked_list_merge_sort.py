#
#  Data Structures: Linked List Merge Sort: The Conquer Step
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

    Runs in O(kn log n) time.
    '''
    if linked_list.size() == 1:
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
    Takes O(k log n) quasilinear time.
    '''
    if linked_list == None or linked_list.head == None:
        left_half = linked_list
        right_half = None
        return left_half, right_half
    else: # non-empty linked lists
        size = linked_list.size()
        midpoint = size // 2
        mid_node = linked_list.node_at_index(midpoint-1)

        left_half = linked_list
        right_half = LinkedList()
        right_half = mid_node.next_node
        mid_node.next_node = None
        return left_half, right_half

def merge(left, right):
    '''
    Merges two linked lists, sorting by data in nodes.
    Returns a new, merged list.
    Runs in O(n) linear time.
    '''
    # Create a new linked list that contains nodes from 
    # merging left and right 
    merged = LinkedList()

    # Add a fake head that is discarded later to simplify code
    merged.add(0)

    # Set current to the head of the linked list
    current = merged.head

    # Obtain head nodes for left and right linked lists
    left_head = left.head
    right_head = right.head

    # Iterate over left and right until we reach the tail node 
    # of either
    while left_head or right_head:
        # If the head node of the left is None, we're past the tail
        # Add the node from right to merged linkned list
        if left_head is None:
            current.next_node = right_head
            # Call next on right to set loop condition to False
            right_head = right_head.next_node
        # If the head node of right is None, we're past the tail
        # Add the tail node from left to merged linked list
        elif right_head is None:
            current.next_node = left_head
             # Call next on left to set loop condition to False
            left_head = left_head.next_node
        else:
            # Not at either tail node
            # Obtain node data to perform comparison operations
            left_data = left_head.data
            right_data = right_head.data
            # If data on left is less than right, set current to left node
            if left_data < right_data:
                current.next_node = left_head
                # Move left head to next node
                left_head = left_head.next_node
            # If data on left is greater than right, set current to right node
            else:
                current.next_node = right_head
                # Move right head to next node
                right_head = right_head.next_node
        # Move current to next node
        current = current.next_node
        
        # Discard fake head and set first merged node as head
        head = merged.head.next_node
        merged.head = head

        return merged

l = LinkedList()
l.add(10)
l.add(2)
l.add(44)
l.add(15)
l.add(200)
print(l)
sorted_linked_list = merge_sort(l)
print(sorted_linked_list)
