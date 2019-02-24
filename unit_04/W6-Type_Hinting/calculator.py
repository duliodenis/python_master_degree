#
#  Python Type Hinting: Built-in Types 
#  Python Techdegree
#
#  Created by Dulio Denis on 2/24/19.
#  Copyright (c) 2019 ddApps. All rights reserved.
# ------------------------------------------------
#  The simplest type hinting is by using the built-in types. 
#  Let's see how to hint functions that are only concerned 
#  with the built-in types.
from numbers import Real

def add(num1: complex, num2: complex) -> complex:
    return num1 + num2


def subtract(num1: Real, num2: Real) -> Real:
    return num1 - num2


def multiply(num1: int, num2: int) -> int:
    return num1 * num2


def divide(num1: int, num2: int) -> float:
    return num1 / num2

print(add(5, 8.2))
print(add('hello', 'world'))
print(multiply('hello ', 5))
