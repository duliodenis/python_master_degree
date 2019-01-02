#
#  Dates and Times in Python: Dates & Time
#  Python Techdegree
#
#  Created by Dulio Denis on 12/24/18.
#  Copyright (c) 2018 ddApps. All rights reserved.
# ------------------------------------------------
#  Challenge 3: Timedelta Minute
# ------------------------------------------------
#  Challenge Task 1 of 1
#  Write a function named minutes that takes two datetimes 
#  and, using timedelta.total_seconds() to get the number 
#  of seconds, returns the number of minutes, rounded, 
#  between them. 
#  The first will always be older and the second newer. 
#  You'll need to subtract the first from the second.
import datetime
import math


def minutes(datetime_older, datetime_newer):
    delta = datetime_newer - datetime_older
    print("delta = {}".format(delta))
    print("delta seconds = {}".format(delta.total_seconds()))
    return math.ceil((delta.total_seconds() * 60 )/ 3600)

# TEST
older = datetime.datetime.now()
twenty_minutes = datetime.timedelta(minutes=20)
newer = older + twenty_minutes

print(older)
print(newer)

print(minutes(older, newer))
