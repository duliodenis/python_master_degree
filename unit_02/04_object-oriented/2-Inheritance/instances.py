#
#  Object-Oriented Python: Inheritance Instances
#  Python Techdegree
#
#  Created by Dulio Denis on 12/14/18.
#  Copyright (c) 2018 ddApps. All rights reserved.
# ------------------------------------------------
#  Challenge Task 1 of 1
#  Alright, here's a fun task!
#  Create a function named combiner that takes a single argument, 
#  which will be a list made up of strings and numbers.
#  Return a single string that is a combination of all of the strings 
#  in the list and then the sum of all of the numbers.
#  For example, with the input ["apple", 5.2, "dog", 8], 
#  combiner would return "appledog13.2". 
#  Be sure to use isinstance to solve this as I might try to trick you.
def combiner(the_list):
    sum = 0
    big_string = ""
    for item in the_list:
        if isinstance(item, str):
            big_string += item
        elif isinstance(item, (int, float,)):
            sum += item
    return big_string+"{}".format(sum)

print(combiner(["apple", 5.2, "dog", 8]))
