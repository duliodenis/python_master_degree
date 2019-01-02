#
#  Dates and Times in Python: Dates & Time
#  Python Techdegree
#
#  Created by Dulio Denis on 12/24/18.
#  Copyright (c) 2018 ddApps. All rights reserved.
# ------------------------------------------------
#  Challenge 6: Time Tango
# ------------------------------------------------
#  Challenge Task 1 of 1
#  Write a function named time_tango that takes a 
#  date and a time. It should combine them into a
#  datetime and return it.
import datetime
from datetime import time
from datetime import date


def time_tango(dt, tm):
    return datetime.datetime.combine(dt, tm)

# TEST
d = date(2005, 7, 14)
t = time(hour=12, minute=34, second=56, microsecond=0)
print(time_tango(d, t))
