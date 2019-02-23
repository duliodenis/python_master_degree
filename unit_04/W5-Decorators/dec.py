#
#  Python Testing: Python Decorators 
#  Python Techdegree
#
#  Created by Dulio Denis on 1/22/19.
#  Copyright (c) 2019 ddApps. All rights reserved.
# ------------------------------------------------
#  Sometimes you can just write a function or
#  method or class and be done with it.
#  But sometimes you find that you need to wrap
#  your functions or methods or classes in some
#  sort of new behavior. And since you're a good
#  programmer, you don't want to change every
#  function in the same way over and over again.
#  That's not DRY or a good use of your time!
#  Well, when that happens, you just might need
#  a decorator. 
# ------------------------------------------------
from functools import wraps

#  Nested functions
def outer():
    number = 5

    def inner():
        print(number)

    inner()

# prints out 5
outer()
# ------------------------------------------------
#  First-class functions
def apply(func, x, y):
    return func(x, y)

def add(x, y):
    return x + y

def sub(x, y):
    return x - y

print(apply(add, 5, 2))
print(apply(sub, 5, 2))
# ------------------------------------------------
#  Closures
def close():
    x = 10

    def inner():
        print(x)

    return inner

closure = close()
closure()

def add_to_five(num):
    def inner():
        print(num+5)
    return inner

fifteen = add_to_five(10)
fifteen()
# ------------------------------------------------
#  Decorators 
#  functions that accept functions as arguments
#  and they have an inner function that performs
#  some action before returning the accepted function.
#  the outer function is the decorator that returns the
#  inner function.
def logme(func):
    import logging
    logging.basicConfig(level=logging.DEBUG)

    def inner(*args, **kwargs):
        logging.debug("Called {} with args {} and kwargs {}".format(
            func.__name__, args, kwargs))
        return func()
    return inner
    
def print_2():
    print(2)

print_2 = logme(print_2)
print_2()

@logme
def print_4():
    print(4)

print_4()

# ------------------------------------------------
#  More Decorators 
print("--------------------------------------")
def logme2(func):
    import logging
    logging.basicConfig(level=logging.DEBUG)

    @wraps(func)
    def inner(*args, **kwargs):
        logging.debug("Called {} with args {} and kwargs {}".format(
            func.__name__, args, kwargs))
        return func(*args, **kwargs)
    # instead of changing inner to the actual outer func
    # inner.__name__ = func.__name__
    # inner.__doc__ = func.__doc__
    # use wraps from functools
    return inner

@logme2
def sub2(x, y, switch=False):
    if not switch:
        print("{} - {} = {}".format(x, y, x - y))
        return x - y
    else:
        print("{} - {} = {}".format(y, x, y - x))
        return y - x

sub2(5, 2)
sub2(5, 2, switch=True)
print(sub2.__name__)
