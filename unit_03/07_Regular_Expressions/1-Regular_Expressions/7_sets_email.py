#
#  Regular Expressions in Python
#  Python Techdegree
#
#  Created by Dulio Denis on 12/29/18.
#  Copyright (c) 2018 ddApps. All rights reserved.
# ------------------------------------------------
#  Challenge 5: Email
# ------------------------------------------------
#  Challenge Task 1 of 1
#  Create a function named find_emails that takes
#  a string. Return a list of all of the email 
#  addresses in the string.
import re

# Example:
# >>> find_emails("kenneth.love@teamtreehouse.com, @support, ryan@teamtreehouse.com, test+case@example.co.uk")
# ['kenneth.love@teamtreehouse.com', 'ryan@teamtreehouse.com', 'test+case@example.co.uk']

def find_emails(data):
    return re.findall(r'[-\w\d+.]+@[-\w\d.]+', data)

print(find_emails("kenneth.love@teamtreehouse.com, @support, ryan@teamtreehouse.com, test+case@example.co.uk"))
