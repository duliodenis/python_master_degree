#
#  Shopping List v2
#  Python Techdegree
#
#  Created by Dulio Denis on 12/5/18.
#  Copyright (c) 2018 ddApps. All rights reserved.
# ------------------------------------------------
#  Course Project: List Creation Application
#  Add items to a shopping list.
#

import os

# Create a new empty shopping list.
shopping_list = []

def clear_screen():
    os.system("cls" if os.name == 'nt' else 'clear')

# Create a function add_to_list() that declares a parameter named item.
def add_to_list(item):
    # Add the item to the list.
    shopping_list.append(item)
    # User Story: As a User, upon adding an item to the list, I should know
    # the total length of my list, so that I don't over shop.
    # Notify the user that the item was added, and state the number of items in the list currently.
    print("Added. There are now {} item(s) in the shopping list.".format(len(shopping_list)))
    show_list()

# Remove an item from the shopping list.
def remove_from_list():
    show_list()
    what_to_remove = input("What item would you like to remove?\n> ")
    try:
        shopping_list.remove(what_to_remove)
    except:
        pass
    show_list()

# User Story: As a User, I should be able to see the list at any time
# so that I can verify my order.
def show_list():
    clear_screen()
    print("Here is the list:")
    for item in shopping_list:
        print(item)
    print("-" * 30)
    print("DONE | SHOW | REMOVE | HELP")
    print("-" * 30)

# User Story: As a User, I should be able to ask for HELP 
# so that I can understand how to use the application.  
def show_help():
    clear_screen()
    print("What should we pick up at the store?")
    print("""
    Enter 'DONE to stop adding items.
    Enter 'SHOW' to show all items in a list.
    Enter 'REMOVE' to delete an item from your list.
    Enter 'HELP' for this help.
    """)

show_help()  

# User Story: As a User, I should be able to continually be prompted
# so that I can add a grocery item or view my list when I need to.
while True:
    new_item = input("> ")
    # User Story: As a User, I should be able to state when I am DONE,
    # # so that I may print out the list in totality.
    if new_item.upper() == 'DONE' or new_item.upper() == 'QUIT':
        break
    elif new_item.upper() == 'HELP':
        show_help()
        continue
    elif new_item.upper() == 'SHOW':
        show_list()
        continue
    elif new_item.upper() == 'REMOVE':
        remove_from_list()
        continue
    else:
        # User Story: As a User I should be able to add an item to a list.
        add_to_list(new_item)

show_list()


