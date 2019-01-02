#
#  Using Databases in Python: Meet Peewee
#  Python Techdegree
#
#  Created by Dulio Denis on 1/1/19.
#  Copyright (c) 2019 ddApps. All rights reserved.
# ------------------------------------------------
#  Challenge 2: First Queries
# ------------------------------------------------
#  Challenge Task 1 of 4
#  Import the Challenge class from models.py.
from models import Challenge

# ------------------------------------------------
#  Challenge Task 2 of 4
#  Now, create a variable named all_challenges. 
#  It should select all of the available challenges 
#  from the database.
all_challenges = Challenge.select()

# ------------------------------------------------
#  Challenge Task 3 of 4
#  Next, create a new Challenge. 
#  The language should be "Ruby", the name should be "Booleans".
Challenge.create(language='Ruby', name='Booleans')

# ------------------------------------------------
#  Challenge Task 4 of 4
#  Finally, make a variable named sorted_challenges
#  that is all of the Challenge records, ordered by
#  the steps attribute on the model. 
#  The order should be ascending, which is the default direction.
sorted_challenges = Challenge.select().order_by(Challenge.steps)

