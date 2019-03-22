#
#  Functional Python: The Lambda Lambada (Recursion)
#  Python Techdegree
#
#  Created by Dulio Denis on 3/22/19.
#  Copyright (c) 2019 ddApps. All rights reserved.
# ------------------------------------------------
#  Recursion Challenge
# ------------------------------------------------
#  Challenge Task 1 of 1
#  Finish the prereqs function so that it recursively
#  finds all of the prerequisite course titles in courses
#  (like "Object-Oriented Python" is a prerequisite for
#  "Django Basics").
#  You should add() the title of the prerequisite to the pres
#  set and then call prereqs again with the child courses.
#  In the end, return the prereqs set.
courses = {'count': 2,
           'title': 'Django Basics',
           'prereqs': [{'count': 3,
                     'title': 'Object-Oriented Python',
                     'prereqs': [{'count': 1,
                               'title': 'Python Collections',
                               'prereqs': [{'count':0,
                                         'title': 'Python Basics',
                                         'prereqs': []}]},
                              {'count': 0,
                               'title': 'Python Basics',
                               'prereqs': []},
                              {'count': 0,
                               'title': 'Setting Up a Local Python Environment',
                               'prereqs': []}]},
                     {'count': 0,
                      'title': 'Flask Basics',
                      'prereqs': []}]}


def prereqs(data, pres=None):
    pres = pres or set()
    # for each prereq in this courses' prereq
    for prereq in data['prereqs']:
        # add title of this prereq course
        pres.add(prereq['title'])
        # use recursive call to drill into any further prereqs
        prereqs(prereq, pres)
    return pres

print(prereqs(courses))
