#
#  Using Databases in Python: Gettin' CRUD-y With It
#  Python Techdegree
#
#  Created by Dulio Denis on 1/5/19.
#  Copyright (c) 2019 ddApps. All rights reserved.
# ------------------------------------------------
#  Challenge 2: CRUD: Search function
# ------------------------------------------------
#  Challenge Task 1 of 1
#  Create a function named search_challenges that
#  takes two arguments, name and language.
#  Return all Challenges where the name field contains
#  name argument and the language field is equal to
#  the language argument. Use == for equality.
#  You don't need boolean and or binary & for this,
#  just put both conditions in your where().
from models import Challenge


def create_challenge(name, language, steps=1):
    Challenge.create(name=name,
                     language=language,
                     steps=steps)

def search_challenges(name, language):   
    return Challenge.select().where((Challenge.name==name) | (Challenge.language==language))
