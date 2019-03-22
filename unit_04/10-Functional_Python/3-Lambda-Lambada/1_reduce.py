#
#  Functional Python: The Lambda Lambada (Reduce)
#  Python Techdegree
#
#  Created by Dulio Denis on 3/22/19.
#  Copyright (c) 2019 ddApps. All rights reserved.
# ------------------------------------------------
#  Quite often we have an iterable that has an
#  answer in it.
#  How do we get that answer out, though?
#  Let's look at `reduce()` and the concept of recursion.
from functools import reduce

def product(x, y):
    return x * y

print(reduce(product, [1,2,3,4,5]))

# Same as the following iterative version:
total = 1
for x in [1,2,3,4,5]:
    total = total * x

print(total)

# Same as the following recursive version:
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)

print(factorial(5))
