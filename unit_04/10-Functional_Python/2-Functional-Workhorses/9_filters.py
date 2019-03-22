#
#  Functional Python: Filter
#  Python Techdegree
#
#  Created by Dulio Denis on 3/21/19.
#  Copyright (c) 2019 ddApps. All rights reserved.
# ------------------------------------------------
#  Filter Challenge
# ------------------------------------------------
#  Challenge Task 1 of 3
#  Write a function named is_2012 that accepts a
#  single argument and returns whether that argument's
#  year attribute is equal to 2012.
import datetime

dates = [
    datetime.datetime(2012, 12, 15),
    datetime.datetime(1987, 8, 20),
    datetime.datetime(1965, 2, 28),
    datetime.datetime(2015, 4, 29),
    datetime.datetime(2012, 6, 30),
]

def is_2012(d):
    if d.year == 2012:
        return True
    return False

print(is_2012(dates[0]))
print(is_2012(dates[1]))

# ------------------------------------------------
#  Challenge Task 2 of 3
#  Now create a variable named dt_2012 that uses
#  filter() and is_2012 to return only the datetimes
#  from dates that are from the year 2012.
dt_2012 = list(filter(is_2012, dates))
print(len(dates))
print(len(dt_2012))


# ------------------------------------------------
#  Challenge Task 3 of 3
#  Create a variable named y_words that uses a list
#  comprehension to only contain the words from words
#  that start with the letter "y".
words = [
    'yellow',
    'red',
    'yesterday',
    'tomorrow',
    'maybe',
    'zucchini',
    'eggplant',
    'year',
    'month',
    'yell',
    'yonder',
    'today',
]

y_words = [word for word in words if word[0] == 'y']
print(y_words)
