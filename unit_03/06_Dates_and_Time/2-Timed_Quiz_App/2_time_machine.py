#
#  Dates and Times in Python: Dates & Time
#  Python Techdegree
#
#  Created by Dulio Denis on 12/24/18.
#  Copyright (c) 2018 ddApps. All rights reserved.
# ------------------------------------------------
#  Challenge 2: Harder Time Machine
# ------------------------------------------------
#  Challenge Task 1 of 1
#  Write a function named time_machine that takes
#  an integer and a string of "minutes", "hours",
#  "days", or "years". This describes a timedelta.
#  Return a datetime that is the timedelta's duration
#  from the starter datetime.
import datetime

starter = datetime.datetime(2015, 10, 21, 16, 29)

# Remember, you can't set "years" on a timedelta!
# Consider a year to be 365 days.

## Example
# time_machine(5, "minutes") => datetime(2015, 10, 21, 16, 34)

def time_machine_v1(num, time_string):
    future_date = None
    if time_string == "minutes":
        minutes = 34 + num
        future_date = datetime.datetime.replace(starter, minute=minutes)
    elif time_string == "hours":
        hours = 16 + num
        future_date = datetime.datetime.replace(starter, hour=hours)
    elif time_string == "days":
        days = num + 21
        future_date = datetime.datetime.replace(starter, day=num)
    elif time_string == "years":
        days = num*365
        future_date = datetime.datetime.replace(starter, day=days)
    return future_date - starter


def time_machine(length_time, time_string):
    if time_string == 'years':
        return starter + datetime.timedelta(days=(length_time * 365))
    else:
        # constructed a dict to use as a kwargs argument:
        return starter + datetime.timedelta(**{time_string: length_time})

# TEST
print(time_machine(5, "minutes"))
