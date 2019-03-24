#
#  Data Structures: Linked Lists: Removing a Node
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
        '''
        Determines if the linked list is empty.
        Takes O(1) time.
        '''
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

    def insert(self, data, index):
        '''
        Inserts a new node containing data at position index.
        Insertion takes O(1) constant time but finding the node at the insertion point takes O(n) linear time.
        Takes overall O(n) linear time.
        '''
        if index == 0:
            self.add(data)
        if index > 0:
            new = Node(data)

            position = index
            current = self.head

            while position > 1:
                current = current.next_node
                position -= 1

            prev_node = current
            next_node = current.next_node

            prev_node.next_node = new
            new.next_node = next_node

    def remove(self, key):
        '''
        Removes the node containing the data that matches the key.
        Returns the node or None if the key doesn't exist.
        Takes O(n) linear time.
        '''
        current = self.head
        previous = None
        found = False

        while current and not found:
            if current.data == key and current == self.head:
                found = True
                self.head = current.next_node
            elif current.data == key:
                found = True
                previous.next_node = current.next_node
            else:
                previous = current
                current = current.next_node
        return current

    def print(self):
        '''
        Returns a string representation of the list.
        Takes O(n) linear time.
        '''
        print("The list: ", end= ""),
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

print("\nSearching for 20")
found_node = list.search(20)
print(found_node.data)

print("\nInserting 15 at index 2")
list.insert(15, 2)
list.print()

print("\nRemoving 10")
list.remove(10)
list.print()
