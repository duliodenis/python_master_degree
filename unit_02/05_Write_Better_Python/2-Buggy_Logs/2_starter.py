#
#  Object-Oriented Python: Write Better Python
#  Python Techdegree
#
#  Created by Dulio Denis on 12/23/18.
#  Copyright (c) 2018 ddApps. All rights reserved.
# ------------------------------------------------
#  Challenge 2: PDB
# ------------------------------------------------
#  Challenge Task 1 of 1
#  Import PDB and call set_trace() where it's needed.

def something_silly(arg1, arg2):
    if len(arg1) > len(arg2):
        # Import and use PDB here
        arg1[0] = arg2[0]
    return arg1, arg2

# ------------------------------------------------

def something_silly(arg1, arg2):
    if len(arg1) > len(arg2):
        # Import and use PDB here
        import pdb; pdb.set_trace()
        arg1[0] = arg2[0]
    return arg1, arg2
