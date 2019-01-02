#
#  Dates and Times in Python: Dates & Time
#  Python Techdegree
#
#  Created by Dulio Denis on 12/24/18.
#  Copyright (c) 2018 ddApps. All rights reserved.
# ------------------------------------------------
#  Challenge 5: Wikipedia app homework.
# ------------------------------------------------
#  Using the Python docs, and strftime and
#  strptime, make a script that accepts a month and
#  day date in whatever format you want that returns 
#  a link to Wikipedia for that date.
#  Be sure you tell the user how to format their data for you.
import datetime


answer_format = "%m/%d"
link_format = "%b_%d"
link = "https://en.wikipedia.org/wiki/{}"

while True:
    answer = input("What date would you like? Please use the MM/DD format. Enter 'Q' to Quit. > ")
    if answer.upper() == 'Q':
        break
    try:
        date = datetime.datetime.strptime(answer, answer_format)
        output = link.format(date.strftime(link_format))
        print(output)
    except ValueError:
        print("That's not a valid date. Please try again.")
