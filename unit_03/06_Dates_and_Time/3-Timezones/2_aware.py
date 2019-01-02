#
#  Dates and Times in Python: Timezones
#  Python Techdegree
#
#  Created by Dulio Denis on 12/25/18.
#  Copyright (c) 2018 ddApps. All rights reserved.
# ------------------------------------------------
#  Challenge 2: Datetime Awareness
# ------------------------------------------------
#  Challenge Task 1 of 2
#  naive is a datetime with no timezone. 
#  Create a new timezone for US/Pacific, which is 
#  8 hours behind UTC (UTC-08:00).
#  Then make a new variable named hill_valley that
#  is naive with its tzinfo attribute replaced with
#  the US/Pacific timezone you made.
import datetime


naive = datetime.datetime(2015, 10, 21, 4, 29)
pacific = datetime.timezone(datetime.timedelta(hours=-8))
hill_valley = naive.astimezone(pacific)

# ------------------------------------------------
# Challenge Task 2 of 2
# Great, but replace just sets the timezone, it doesn't 
# move the datetime to the new timezone. Let's move one.
# Make a new timezone that is UTC+01:00.
# Create a new variable named paris that uses your new 
# timezone and the astimezone method to change hill_valley to the new timezone.
paris_tz = datetime.timezone(datetime.timedelta(hours=+1))
hill_valley = datetime.datetime(2015, 10, 21, 4, 29, tzinfo=pacific)
paris = hill_valley.astimezone(paris_tz)
