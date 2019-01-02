#
#  Python File I/O Workshop
#  Python Techdegree
#
#  Created by Dulio Denis on 12/30/18.
#  Copyright (c) 2018 ddApps. All rights reserved.
# ------------------------------------------------
#  You often need to write to a file to store data
#  for later use. 
#  Python makes this really straightforward!
# ------------------------------------------------
import sys

def rememberer(thing):
    # open file
    file = open("database.txt", "a")

    # write thing to file
    file.write(thing+"\n")

    # close file
    file.close()

# context manager pattern for dealing with files
def rememberer_with(thing):
    with open("database.txt", "a") as file:
        file.write(thing+"\n")

def show():
    # open file using a context manager
    with open("database.txt") as file:
        # print out each line in file
        for line in file:
            print(line)

if __name__ == '__main__':
    if sys.argv[1].lower() == "--list":
        show()
    else: 
        # rememberer_with(input("What should I remember? > "))
        rememberer_with(' '.join(sys.argv[1:]))
