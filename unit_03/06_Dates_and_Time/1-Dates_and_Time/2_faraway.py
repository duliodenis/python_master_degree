#
#  Dates and Times in Python: Dates & Time
#  Python Techdegree
#
#  Created by Dulio Denis on 12/24/18.
#  Copyright (c) 2018 ddApps. All rights reserved.
# ------------------------------------------------
#  Challenge 2: Far Away
# ------------------------------------------------
#  Challenge Task 1 of 1
#  Write a function called far_away that takes one
#  argument, a timedelta. Add that timedelta to 
#  datetime.datetime.now() and 
#  return the resulting datetime object.
import datetime


def far_away(td):
    return datetime.datetime.now() + td

# TEST
td = datetime.timedelta(days=2)
print(far_away(td))
