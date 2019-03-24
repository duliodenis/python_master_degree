#
#  Data Structures: Linked Lists
#  Python Techdegree
#
#  Created by Dulio Denis on 3/24/19.
#  Copyright (c) 2019 ddApps. All rights reserved.
# ------------------------------------------------
class Node:
    '''
    An object for storing a single node of a linked list.
    Models two attributes - data and the link to the next node in the list.

    Attributes:
        data: Data stored in node
        next_node: Reference to next node in linked list
    '''
    data = None
    next_node = None

    def __init__(self, data, next_node = None):
        self.data = data
        self.next_node = next_node

N1 = Node(10)

N2 = Node(20)
N1.next_node = N2

print(N1.data)
print(N1.next_node.data)

class SinglyLinkedList:
    '''
    Linear data structure that stores values in nodes.

    Attributes:
        head: The head node of the list
    '''
    def __init__(self):
        self.head = None
    
    def is_empty(self):
        return self.head == None
    
    def size(self):
        '''
        Returns the number of nodes in the list.
        Takes O(n) linear time.
        '''
        current = self.head
        count = 0

        while current:
            count += 1
            current = current.next_node
        return count

list = SinglyLinkedList()
