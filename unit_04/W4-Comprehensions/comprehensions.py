#
#  Python Testing: Python Comprehensions 
#  Python Techdegree
#
#  Created by Dulio Denis on 1/21/19.
#  Copyright (c) 2019 ddApps. All rights reserved.
# ------------------------------------------------
#  Comprehensions are a convenient way to work with
#  iterables in Python. Comprehensions let you skip
#  the for loop and start creating lists, dicts,
#  and sets straight from your iterables.
#  Comprehensions also let you emulate functional
#  programming aspects like map() and filter() in
#  a more accessible way. 
# ------------------------------------------------
list_comprension = [num * 2 for num in range(1, 6)]
# [2, 4, 6, 8, 10, 12]
print(list_comprension)

dict_comprehension = {letter: num for letter, num in zip('abcdef', range(1, 7))}
# {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}
print(dict_comprehension)

set_comprehension = {num * 2 for num in [5, 2, 18, 2, 42, 2, 2]}
# {84, 10, 4, 36}
print(set_comprehension)
