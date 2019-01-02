#
#  CSV and JSON in Python Workshop: Art
#  Python Techdegree
#
#  Created by Dulio Denis on 12/30/18.
#  Copyright (c) 2018 ddApps. All rights reserved.
# ------------------------------------------------
#  JSON is quickly becoming the de facto standard
#  for Web-based communication. Most APIs expect,
#  accept, and return JSON and many pieces of
#  desktop software use JSON for configuration files.
#  Let's see how to use Python's built-in `json`
#  module to read and write this handy format.
# ------------------------------------------------
import json

with open('148.json') as artfile:
    art = json.load(artfile)
    print(art['description'])

nums = json.loads("[1, 2, 3]")
print(nums[2])

num_string = json.dumps([5, 4, 3, 2, 1])
print(num_string)

me = {'first_name': 'Kenneth', 'last_name': 'Love', 'topic': 'Python'}
string_me = str(me)
json_dumps_me = json.dumps(me)

print(string_me)
print("vs")
print(json_dumps_me)

