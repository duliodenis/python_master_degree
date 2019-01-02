#
#  Regular Expressions in Python
#  Python Techdegree
#
#  Created by Dulio Denis on 12/29/18.
#  Copyright (c) 2018 ddApps. All rights reserved.
# ------------------------------------------------
#  Challenge 8: Email Groups
# ------------------------------------------------
#  Challenge Task 1 of 2
#  Create a new variable named contacts that is an
#  re.search() where the pattern catches the email
#  address and phone number from string. Name the
#  email pattern email and the phone number pattern
#  phone. The comma and spaces * should not* be part
#  of the groups.
import re

string = '''Love, Kenneth, kenneth+challenge@teamtreehouse.com, 555-555-5555, @kennethlove
Chalkley, Andrew, andrew@teamtreehouse.co.uk, 555-555-5556, @chalkers
McFarland, Dave, dave.mcfarland@teamtreehouse.com, 555-555-5557, @davemcfarland
Kesten, Joy, joy@teamtreehouse.com, 555-555-5558, @joykesten'''

contacts = re.search(r'''
    (?P<email>[-\w\d.+]+@[-\w\d.]+)
    ,\s
    (?P<phone>\d{3}-\d{3}-\d{4})
''',string,re.X | re.M)

print(contacts)

# ------------------------------------------------
#  Challenge Task 2 of 2
#  Great! Now, make a new variable, twitters that is
#  an re.search() where the pattern catches the Twitter
#  handle for a person. Remember to mark it as being
#  at the end of the string. 
#  You'll also want to use the re.MULTILINE flag.
twitters = re.search(r'''
    (?P<twitter_handle>@[\w\d]+)$
''', string, re.X | re.M)

print(twitters)
