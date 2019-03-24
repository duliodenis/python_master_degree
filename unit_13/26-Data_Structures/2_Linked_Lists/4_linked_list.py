#
#  Data Structures: Linked Lists: Implementing Search
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

    def add(self, data):
        '''
        Adds a new head node to the list with data.
        Takes O(1) constant time.
        '''
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node

    def search(self, key):
        '''
        Search for the first node that matches the key.
        Returns the node or None if not found.
        Takes O(n) linear time.
        '''
        current = self.head
        while current:
            if current.data == key:
                return current
            else:
                current = current.next_node
        return None

    def print(self):
        '''
        Returns a string representation of the list.
        Takes O(n) linear time.
        '''
        print("The list:")
        current = self.head
        while current:
            print("{} -> ".format(current.data), end=""),
            current = current.next_node
        print("None")

list = SinglyLinkedList()
list.head = N1
list.add(30)
print(list.head.data)
print(list.size())
list.print()

found_node = list.search(20)
print(found_node.data)
