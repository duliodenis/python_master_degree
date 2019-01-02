#
#  Regular Expressions in Python: Reading Files
#  Python Techdegree
#
#  Created by Dulio Denis on 12/26/18.
#  Copyright (c) 2018 ddApps. All rights reserved.
# ------------------------------------------------
#  Before we can search through our text, we have 
#  to be able to open the file it's contained in. 
#  Then we can start with some super-specific 
#  searches of our text.
# ------------------------------------------------
import re

name_file = open("names.txt", encoding="utf-8")

print(name_file)
print("------------------------------")

data = name_file.read()
name_file.close()

# print(data)

first_name = r'Kenneth'

print(re.match(r'Love', data))
print(re.match(first_name, data))
print(re.search(first_name, data))
