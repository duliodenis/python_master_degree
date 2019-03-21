#
#  Functional Python: Map & Filter
#  Python Techdegree
#
#  Created by Dulio Denis on 3/21/19.
#  Copyright (c) 2019 ddApps. All rights reserved.
# ------------------------------------------------
#  Map & Filter Challenge
# ------------------------------------------------
#  Challenge Task 1 of 3
#  Create a function named is_over_13 that takes
#  a datetime and returns whether or not the difference
#  between that datetime and today is 4745 days or more.
import datetime

birthdays = [
    datetime.datetime(2012, 4, 29),
    datetime.datetime(2006, 8, 9),
    datetime.datetime(1978, 5, 16),
    datetime.datetime(1981, 8, 15),
    datetime.datetime(2001, 7, 4),
    datetime.datetime(1999, 12, 30)
]

today = datetime.datetime.today()

def is_over_13(d):
    return (datetime.datetime.now() - d) >= datetime.timedelta(days=4745)

print(is_over_13(birthdays[0]))


# ------------------------------------------------
#  Challenge Task 2 of 3
#  Now create a function named date_string that takes
#  a datetime and returns a string like "May 20" using
#  strftime. The format string is "%B %d".
def date_string(d):
    return d.strftime("%B %d")

print(date_string(birthdays[0]))

# ------------------------------------------------
#  Challenge Task 3 of 3
#  Finally, make a variable named birth_dates. 
#  Use map() and filter(), along with your two functions,
#  to create date strings for every datetime in birthdays
#  so long as the datetime is more than 13 years old.
birth_dates = list(map(date_string, filter(is_over_13, birthdays)))
print(birth_dates)

# NOTE: You don't include the parameters in the function as the first argument.
#       You don't need "(d)". 
#       For both map and filer, you need to put just the name of the function
#       as the first argument and then the iterable that you want to pass as an
#       argument to the function as the second argument. 
#       In the code above, the filter function is used as the second argument
#       to return only the birthdays that are over 13 to be used in the date_string
#       function.
