#
#  Using Databases in Python: Gettin' CRUD-y With It
#  Python Techdegree
#
#  Created by Dulio Denis on 1/5/19.
#  Copyright (c) 2019 ddApps. All rights reserved.
# ------------------------------------------------
#  Challenge 3: CRUD: Delete function
# ------------------------------------------------
#  Challenge Task 1 of 1
#  Create a function named delete_challenge that
#  takes a Challenge as an argument. Delete the
#  specified Challenge. 
#  Your function shouldn't return anything.
from models import Challenge


def create_challenge(name, language, steps=1):
    Challenge.create(name=name,
                     language=language,
                     steps=steps)


def search_challenges(name, language):
    return Challenge.select().where(
        Challenge.name.contains(name),
        Challenge.language==language
    )

def delete_challenge(challenge):
    challenge.delete_instance()
