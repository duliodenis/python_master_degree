#
#  Dates and Times in Python: Dates & Time
#  Python Techdegree
#
#  Created by Dulio Denis on 12/24/18.
#  Copyright (c) 2018 ddApps. All rights reserved.
# ------------------------------------------------
#  Challenge 1: Simple Time Machine
# ------------------------------------------------
#  Challenge Task 1 of 1
#  Write a function named delorean that takes an integer. 
#  Return a datetime that is that many hours ahead from starter.
import datetime

starter = datetime.datetime(2015, 10, 21, 16, 29)

def delorean(num):
    if num+16 > 23:
        return datetime.datetime.replace(starter, day=22, hour=num)        
    return datetime.datetime.replace(starter, hour=16+num)

# TEST
print(delorean(10))