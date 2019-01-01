#
#  Dungeon Game: Mapping
#  Python Techdegree
#
#  Created by Dulio Denis on 12/12/18.
#  Copyright (c) 2018 ddApps. All rights reserved.
# ------------------------------------------------
# Challenge Task 1 of 1
# OK, here's a...weird...set of tiles. 
# I need you to loop through TILES and print out each item. 
# Print each item on the same line unless the item is a double pipe (||). 
# In that case, instead of printing the item, print a new line (\n). 
# Use the end argument to print() to control whether things print on a new line or not.

TILES = ('-', ' ', '-', ' ', '-', '||',
         '_', '|', '_', '|', '_', '|', '||',
         '&', ' ', '_', ' ', '||',
         ' ', ' ', ' ', '^', ' ', '||'
)

for tile in TILES:
    if tile == '||':
        print()
    else:
        print(tile, end="")
    

