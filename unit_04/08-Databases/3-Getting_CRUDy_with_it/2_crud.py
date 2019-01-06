#
#  Using Databases in Python: Gettin' CRUD-y With It
#  Python Techdegree
#
#  Created by Dulio Denis on 1/5/19.
#  Copyright (c) 2019 ddApps. All rights reserved.
# ------------------------------------------------
#  Challenge 1: CRUD: Create Function
# ------------------------------------------------
#  Challenge Task 1 of 1
#  Create a function named create_challenge() that
#  takes name, language, and steps arguments. 
#  Steps should be optional, so give it a default
#  value of 1. Create a Challenge from the arguments.
#  create_challenge should not return anything.
from models import Challenge

def create_challenge(name, language, steps=1):
    Challenge.create(name=name, language=language, steps=steps)
