#
#  *args pattern challenge
#  Python Techdegree
#
#  Created by Dulio Denis on 12/10/18.
#  Copyright (c) 2018 ddApps. All rights reserved.
# ------------------------------------------------
#  Let's play with the *args pattern.
#  Create a function named multiply that takes any number of arguments. 
#  Return the product (multiplied value) of all of the supplied arguments. 
#  The type of argument shouldn't matter.
#  Slices might come in handy for this one.
def multiply(*args):
    product = 1
    for factor in args:
        product *= factor
    return product

print(multiply(5, 10))
print(enumerate("abc"))