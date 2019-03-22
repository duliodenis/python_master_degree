#
#  Functional Python: The Lambda Lambada (Lambdas)
#  Python Techdegree
#
#  Created by Dulio Denis on 3/22/19.
#  Copyright (c) 2019 ddApps. All rights reserved.
# ------------------------------------------------
#  Anonymous functions are great for single-use functions.
#  And they have a really fun name, lambdas!
# ------------------------------------------------
#  lambda, like def, is the keyword that marks a new function.
#  Lambda functions don't have to have a name, though.
#  Lambdas can't contain new lines (outside of containers) or assignments.
from functools import reduce

def product(x, y):
    return x * y

print(reduce(product, [1,2,3,4,5]))

# Now do it with a lambda
print(reduce(lambda x, y: x * y, [1,2,3,4,5]))
