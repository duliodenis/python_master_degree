#
#  Object-Oriented Python: Inheritance Inventory
#  Python Techdegree
#
#  Created by Dulio Denis on 12/14/18.
#  Copyright (c) 2018 ddApps. All rights reserved.
# ------------------------------------------------
#  Challenge Task 1 of 3
#  I've made you a super-simple Inventory class that would let someone store items in it. 
#  Not the most useful class, but we'll build something better in a few videos.
#  For now, though, I need you to create a new class, SortedInventory that should be a subclass of Inventory.
#  You can just put pass in the body of your class for this step.
class Inventory:
    def __init__(self):
        self.slots = []

    def add_item(self, item):
        self.slots.append(item)

class SortedInventory(Inventory):
    pass

# Challenge Task 2 of 3
# Great! Now override the add_item method. Use super() in it to make sure the item still gets added to the list.
class SortedInventory(Inventory):
    def add_item(self, item):
        super().add_item(item)

# Challenge Task 3 of 3
# Sorted inventories should be just that: sorted. 
# Right now, we just add an item onto the slots list whenever our add_item method is called. 
# Use the list.sort() method to make sure the slots list gets sorted after an item is added. 
# Only do this in the SortedInventory class.
class SortedInventory(Inventory):
    def add_item(self, item):
        super().add_item(item)
        self.slots.sort()
