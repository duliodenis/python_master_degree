#
#  Dates and Times in Python: Dates & Time
#  Python Techdegree
#
#  Created by Dulio Denis on 12/24/18.
#  Copyright (c) 2018 ddApps. All rights reserved.
# ------------------------------------------------
#  Challenge 1: now() and replace()
# ------------------------------------------------
#  Challenge Task 1 of 4
#  Import the datetime library.
import datetime

#  Challenge Task 2 of 4
#  Create a variable named now that holds the 
#  results of datetime.datetime.now().
now = datetime.datetime.now()

#  Challenge Task 3 of 4
#  Create a new variable called two that holds the 
#  value of now with the hour set to 14. Use the .replace() method.
two = now.replace(hour=14)

#  Challenge Task 4 of 4
#  Finally, change two so its minute is 30.
two = two.replace(minute=30)
