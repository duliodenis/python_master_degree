#
#  Python Testing: First Steps with Testing 
#  Python Techdegree
#
#  Created by Dulio Denis on 1/6/19.
#  Copyright (c) 2019 ddApps. All rights reserved.
# ------------------------------------------------
#  Doctests are the simplest tests to write in 
#  Python since they're written in plain text in
#  the docstrings you're already writing for your
#  code.
# ------------------------------------------------
#
#  Run on the command line with: 
#  >> python3 -m doctest 1_area.py
#
# Failed Test test since 5 * 5 = 25 and not 21
#
def area(width, height):
    '''Return the area as calculated by multiplying 
       width x height. 

    >>> area(5,5)
    21

    '''
    return width * height

print(area(6, 6))

