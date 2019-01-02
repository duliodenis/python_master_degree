#
#  Dates and Times in Python: Dates & Time
#  Python Techdegree
#
#  Created by Dulio Denis on 12/24/18.
#  Copyright (c) 2018 ddApps. All rights reserved.
# ------------------------------------------------
#  Challenge 4: strftime & strptime
# ------------------------------------------------
#  Challenge Task 1 of 2
#  Create a function named to_string that takes a 
#  datetime and gives back a string in the format
#  "24 September 2012".
#  ## Examples
#     to_string(datetime_object) => "24 September 2012"
#     from_string("09/24/12 18:30", "%m/%d/%y %H:%M") => datetime
import datetime


def to_string(dt):
    return dt.strftime("%d %B %Y")

# TEST
dt = datetime.datetime.now()
print(to_string(dt))

#  Challenge Task 2 of 2
#  Create a new function named from_string that takes two arguments: 
#  a date as a string and an strftime-compatible format string, and
#  returns a datetime created from them.
def from_string(date_string, format_string):
    return datetime.datetime.strptime(date_string, format_string)

# TEST
date_string = "24 December 2018"
date_format = "%d %B %Y"
print(from_string(date_string, date_format))
