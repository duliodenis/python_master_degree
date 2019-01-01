#
#  Messy List
#  Python Techdegree
#
#  Created by Dulio Denis on 12/7/18.
#  Copyright (c) 2018 ddApps. All rights reserved.
# ------------------------------------------------
#  Alright, my list is messy! Help me clean it up!
#  First, start by moving the 1 from index 3 to index 0. 
#  Try to do this in a single step by using both .pop() and .insert(). 
#  It's OK if it takes you more than one step, though!
#  
messy_list = ["a", 2, 3, 1, False, [1, 2, 3]]

# Your code goes below here
messy_list.insert(0, messy_list.pop(3))
print(messy_list)

# Great! Now use .remove() and/or del to remove the string, 
# the boolean, and the list from inside of messy_list. 
# When you're done, messy_list should have only integers in it.
messy_list.remove("a")
del messy_list[3]
del messy_list[3]
print(messy_list)