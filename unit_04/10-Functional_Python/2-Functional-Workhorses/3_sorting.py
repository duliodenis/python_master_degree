#
#  Functional Python: Functional Workhorses
#  Python Techdegree
#
#  Created by Dulio Denis on 2/26/19.
#  Copyright (c) 2019 ddApps. All rights reserved.
# ------------------------------------------------
#  Challenge 1: Sorting
# ------------------------------------------------
#  Challenge Task 1 of 3
#  Import itemgetter from the operator module.
from operator import itemgetter

fruit_list = [
    ('apple', 2),
    ('banana', 5),
    ('coconut', 1),
    ('durian', 3),
    ('elderberries', 4)
]

# ------------------------------------------------
#  Challenge Task 2 of 3
# ------------------------------------------------
#  Now create a variable named sorted_fruit that 
#  uses sorted() and itemgetter() to sort fruit_list
#  by the second item in each tuple.
sorted_fruit = sorted(fruit_list, key=itemgetter(1))
print(sorted_fruit)

# ------------------------------------------------
#  Challenge Task 3 of 3
# ------------------------------------------------
#  Use sorted() and attrgetter() to sort date_list
#  by the day attribute of each datetime object.
#  Save this sorting into a variable named sorted_dates.
import datetime
from operator import attrgetter

date_list = [
    datetime.datetime(2015, 4, 29, 10, 15, 39),
    datetime.datetime(2006, 8, 15, 14, 59, 2),
    datetime.datetime(1981, 5, 16, 2, 10, 42),
    datetime.datetime(2012, 8, 9, 14, 59, 2),
]

sorted_dates = sorted(date_list, key=attrgetter('day'))
print(sorted_dates)
