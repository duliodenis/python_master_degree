#
#  Using Databases in Python: Diary App
#  Python Techdegree
#
#  Created by Dulio Denis on 1/4/19.
#  Copyright (c) 2019 ddApps. All rights reserved.
# ------------------------------------------------
#  Challenge 2: OrderedDict Practice
# ------------------------------------------------
#  Challenge Task 1 of 2
#  Import OrderedDict from the collections module.
from collections import OrderedDict

## Menu Items:
# 'n', 'new challenge'
# 's', 'new step'
# 'd', 'delete a challenge'
# 'e', 'edit a challenge'


# ------------------------------------------------
#  Challenge Task 2 of 2
#  Now create an OrderedDict named menu that has
#  the menu items exactly as listed in the comment.
#  Both keys and values will be strings.
menu = OrderedDict([
    ('n', 'new challenge'),
    ('s', 'new step'),
    ('d', 'delete a challenge'),
    ('e', 'edit a challenge'),
])
