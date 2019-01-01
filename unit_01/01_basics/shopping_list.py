#
#  Shopping List App
#  Python Techdegree
#
#  Created by Dulio Denis on 2/5/17.
#  Copyright (c) 2017 ddApps. All rights reserved.
# ------------------------------------------------
#  v1: Shopping List To-Do List
#  - Run the script to start using it
#  - Put new things into the List
#  - Enter the word DONE - in all CAPS - to quit the program
#  - And, once I quit, I want the app to show me everything that's on my List
# ------------------------------------------------
#  v2: Add a HELP and SHOW commane
# ------------------------------------------------
def show_help():
    # print out instructions on how to use the app
    print("What should we do today?")
    print("""
Enter 'DONE' to stop adding items.
Enter 'SHOW' to show your current list.
Enter 'HELP' to show this help.
    """)

def show_list():
    # print out the List
    print("Here is your list:")

    for item in shopping_list:
        print(item)

def add_to_list(new_item):
    # add new items to our List
    shopping_list.append(new_item)
    print("Added {} to the list. The list now has {} item(s).".format(new_item, len(shopping_list)))


# make a list to hold our items
shopping_list = []

show_help()

while True:
    # ask for new items
    new_item = input("> ")

    # be able to quit the app
    if new_item == 'DONE':
        break
    elif new_item == 'HELP':
        show_help()
        continue
    elif new_item == 'SHOW':
        show_list()
        continue

    add_to_list(new_item)

show_list()
