#
#  Object-Oriented Python: Advanced Objects
#  Python Techdegree
#
#  Created by Dulio Denis on 12/15/18.
#  Copyright (c) 2018 ddApps. All rights reserved.
# ------------------------------------------------
#  Subclassing Built-ins Challenge (int)
# ------------------------------------------------
# Challenge Task 1 of 3
# Alright, time to subclass int.
# Make a class named Double that extends int. 
# For now, just put pass inside the class.
  class Double(int):
     pass

# Challenge Task 2 of 3
# Now override __new__. Create a new int instance from 
# whatever is passed in as arguments and keyword arguments. 
# Return that instance.
# You should remove the pass.
class Double(int):
   def __new__(*args, **kwargs):
       self = int.__new__(*args, **kwargs) 
       return self

# Challenge Task 3 of 3
# And, finally, double (multiply by two) the int that you 
# created in __new__. Return the new, doubled value. 
# For example, Double(5) would return a 10.
class Double(int):
   def __new__(*args, **kwargs):
       self = int.__new__(*args, **kwargs) 
       self = self * self
       return self