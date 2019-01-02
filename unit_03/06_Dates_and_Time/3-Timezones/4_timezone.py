#
#  Dates and Times in Python: Timezones
#  Python Techdegree
#
#  Created by Dulio Denis on 12/25/18.
#  Copyright (c) 2018 ddApps. All rights reserved.
# ------------------------------------------------
#  Challenge 4: Timezone Strings
# ------------------------------------------------
#  Challenge Task 1 of 1
#  Create a function named to_timezone that takes a 
#  timezone name as a string. Convert starter to that 
#  timezone using pytz's timezones and return the new 
#  datetime.
import datetime

import pytz

starter = pytz.utc.localize(datetime.datetime(2015, 10, 21, 23, 29))

def to_timezone(timezone_as_string):
    return starter.astimezone(pytz.timezone(timezone_as_string))
