#
#  Object-Oriented Python: Write Better Python
#  Python Techdegree
#
#  Created by Dulio Denis on 12/23/18.
#  Copyright (c) 2018 ddApps. All rights reserved.
# ------------------------------------------------
#  Challenge 5: Docstrings
# ------------------------------------------------
#  Challenge Task 1 of 2
#  Add a docstring to Treehouse.student. It should say "Gives a pleasant message about the student.".
class Treehouse:
    '''Methods related to Treehouse and students.'''
    def student(self, name):
        '''Gives a pleasant message about the student.'''
        return '{} is a great Treehouse student!'.format(name)

# ------------------------------------------------
# Challenge Task 2 of 2
# Add a docstring to Treehouse. Should be "Methods related to Treehouse and students.".
