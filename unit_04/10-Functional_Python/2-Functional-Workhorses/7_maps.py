#
#  Functional Python: Functional Workhorses
#  Python Techdegree
#
#  Created by Dulio Denis on 3/2/19.
#  Copyright (c) 2019 ddApps. All rights reserved.
# ------------------------------------------------
#  Map Comprehension Challenge
# ------------------------------------------------
#  Challenge Task 1 of 2
#  Create a function named area() that takes a single
#  argument which will be a two-member tuple.
#  area() should return the result of multiplying
#  the first item in the tuple by the second item in the tuple.
dimensions = [
    (5, 5),
    (10, 10),
    (2.2, 2.3),
    (100, 100),
    (8, 70),
]

def area(sides):
    return sides[0] * sides[1]

sides_tuple = (10, 20)
print("Area with side of {} and {} = {}".format(sides_tuple[0], sides_tuple[1], area(sides_tuple)))

# ------------------------------------------------
#  Challenge Task 2 of 2
#  Now make a variable named areas that calculates
#  the area of each item in dimensions using your
#  area function. You should do this with a list comprehension.
areas = [area(sides_tuple) for sides_tuple in dimensions]
print(areas)
