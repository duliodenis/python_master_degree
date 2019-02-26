#
#  Functional Python: Functional Workhorses
#  Python Techdegree
#
#  Created by Dulio Denis on 2/26/19.
#  Copyright (c) 2019 ddApps. All rights reserved.
# ------------------------------------------------
#  More than just a friend of Dora or a way to find
#  things, `map()` lets us apply transformations to
#  each item in an iterable.
a = [1,2,3]

def double(n):
    return n * 2

print(list(map(double, a)))
