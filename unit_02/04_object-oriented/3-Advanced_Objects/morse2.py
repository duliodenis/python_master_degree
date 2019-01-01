#
#  Object-Oriented Python: Advanced Objects
#  Python Techdegree
#
#  Created by Dulio Denis on 12/15/18.
#  Copyright (c) 2018 ddApps. All rights reserved.
# ------------------------------------------------
#  Challenge Task 1 of 1
#  Let's make our Letter class better for our Morse code challenge. 
#  Add an __iter__ method to the Letter class so the letter's pattern 
#  can be iterated through. You'll want to use yield or yield from.
#  Do not convert the pattern to dots and dashes in __iter__.
class Letter:
    def __init__(self, pattern=None):
        self.pattern = pattern
      
    def __str__(self):
        output = []
        for blip in self.pattern:
            if blip == '.':
                output.append('dot')
            else:
                output.append('dash')
        return '-'.join(output)

    def __iter__(self):
        for item in self.pattern:
            yield item
    
class S(Letter):
    def __init__(self):
         pattern = ['.', '.', '.']
         super().__init__(pattern)
