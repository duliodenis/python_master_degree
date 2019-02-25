#
#  Functional Python: First-Class Functions
#  Python Techdegree
#
#  Created by Dulio Denis on 2/25/19.
#  Copyright (c) 2019 ddApps. All rights reserved.
# ------------------------------------------------
#  Create a function named apply that should take
#  three arguments: a function and two arguments.
#  apply should return the result of calling the
#  function with the two arguments.
def apply(func, x, y):
    return func(x, y,)

def add(x, y):
    return x + y

a = 5
b = 4
print("Calling apply = {}".format(apply(add, a, b)))
