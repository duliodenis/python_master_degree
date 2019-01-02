#
#  Regular Expressions in Python: Reading Files
#  Python Techdegree
#
#  Created by Dulio Denis on 12/27/18.
#  Copyright (c) 2018 ddApps. All rights reserved.
# ------------------------------------------------
#  Challenge 1: Basics
# ------------------------------------------------
#  Challenge Task 1 of 5
#  Use open() to load the file "basics.txt" into 
#  the variable file_object.
# ------------------------------------------------
file_object = open("basics.txt")

# ------------------------------------------------
# Challenge Task 2 of 5
# Read the contents of file_object into a new 
# variable named data.
data = file_object.read()

# ------------------------------------------------
# Challenge Task 3 of 5
# Now close the file_object file so it isn't taking 
# up memory.
file_object.close()

# ------------------------------------------------
# Challenge Task 4 of 5
# Import re. Create an re.match() for the word "Four" 
# in the data variable. Assign this to a new variable 
# named first.
import re

first = re.match(r"Four", data)

# ------------------------------------------------
# Challenge Task 5 of 5
# Finally, make a new variable named liberty that is 
# an re.search() for the word "Liberty" in our data 
# variable.
liberty = re.search(r'Liberty', data)