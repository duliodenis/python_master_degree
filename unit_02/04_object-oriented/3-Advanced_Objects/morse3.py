#
#  Object-Oriented Python: Advanced Objects
#  Python Techdegree
#
#  Created by Dulio Denis on 12/16/18.
#  Copyright (c) 2018 ddApps. All rights reserved.
# ------------------------------------------------
#  Challenge Task 1 of 1
#  Let's practice using @classmethod!
#  Create a class method in Letter named from_string 
#  that takes a string like "dash-dot" and creates an 
#  instance with the correct pattern (['_', '.']).
# ------------------------------------------------
class Letter:
    def __init__(self, pattern=None):
        self.pattern = pattern
      
    def __iter__(self):
        yield from self.pattern
      
    def __str__(self):
        output = []
        for blip in self:
            if blip == '.':
                output.append('dot')
            else:
                output.append('dash')
        return '-'.join(output)

    @classmethod
    def from_string(cls, message):
        contains = []
        message = message.lower()
        message = message.split("-")
        print(message)
        for item in message:
            if item == "dash".lower():
                contains.append("_")
            elif item == "dot".lower():
                contains.append(".")
        return cls(contains)


class S(Letter):
    def __init__(self):
         pattern = ['.', '.', '.']
         super().__init__(pattern)

l = Letter().from_string("dot-dash")
print(l.pattern)