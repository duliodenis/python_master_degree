#
#  sillyCase
#  Python Techdegree
#
#  Created by Dulio Denis on 12/8/18.
#  Copyright (c) 2018 ddApps. All rights reserved.
# ------------------------------------------------
#  Create a new function for me.
#  This one will be named sillycase and it'll take a single string as an argument.
#  sillycase should return the same string but the first half should be lowercased 
#  and the second half should be uppercased. For example, with the string \"Treehouse\", 
#  sillycase would return \"treeHOUSE\".
#  Don't worry about rounding your halves, but remember that indexes should be integers.
#  You'll want to use the int() function or integer division, //."
def sillyCase(input):
    mid_point = len(input) // 2
    counter = 0
    return_string = ""
    for item in input:
        if counter < mid_point:
            return_string = return_string + input[counter].lower()
        else:
            return_string = return_string + input[counter].upper()
        counter += 1
    return return_string

print(sillyCase("Treehouse"))
