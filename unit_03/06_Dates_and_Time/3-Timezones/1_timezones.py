#
#  Dates and Times in Python: Timezones
#  Python Techdegree
#
#  Created by Dulio Denis on 12/25/18.
#  Copyright (c) 2018 ddApps. All rights reserved.
# ------------------------------------------------
#  Challenge 1: Timezone Maker
# ------------------------------------------------
#  Challenge Task 1 of 3
# ------------------------------------------------
#  Create a variable named moscow that holds a 
#  datetime.timezone object at +4 hours.
import datetime

moscow_tz = datetime.timedelta(hours=4)
moscow = datetime.timezone(moscow_tz)

# ------------------------------------------------
# Challenge Task 2 of 3
# Now create a timezone variable named pacific that holds a timezone at UTC-08:00.
pacific = datetime.timezone(datetime.timedelta(hours=-8))

# ------------------------------------------------
# Challenge Task 3 of 3
# Finally, make a third variable named india that hold's a timezone at UTC+05:30.
india = datetime.timezone(datetime.timedelta(hours=5, minutes=30))