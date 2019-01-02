#
#  Dates and Times in Python: Dates & Time
#  Python Techdegree
#
#  Created by Dulio Denis on 12/24/18.
#  Copyright (c) 2018 ddApps. All rights reserved.
# ------------------------------------------------
#  Challenge 3: Timestamp Ordering
# ------------------------------------------------
#  Challenge Task 1 of 1
#  Create a function named timestamp_oldest that 
#  takes any number of POSIX timestamp arguments. 
#  Return the oldest one as a datetime object.
#  Remember, POSIX timestamps are floats and lists 
#  have a .sort() method.
#  If you need help, look up datetime.datetime.fromtimestamp()
#  Also, remember that you *will not* know how many timestamps
#  are coming in.
import datetime

def timestamp_oldest(*args):
  return datetime.datetime.fromtimestamp(min(args))


