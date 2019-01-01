#
#  Object-Oriented Python: Advanced Objects
#  Python Techdegree
#
#  Created by Dulio Denis on 12/14/18.
#  Copyright (c) 2018 ddApps. All rights reserved.
# ------------------------------------------------
#  Challenge Task 1 of 1
#  Let's use __str__ to turn Python code into Morse code! 
#  OK, not really, but we can turn class instances into a
#  representation of their Morse code counterparts.
#  I want you to add a __str__ method to the Letter class
#  that loops through the pattern attribute of an instance
#  and returns "dot" for every "." (period) and "dash" for
#  every "_" (underscore). Join them with a hyphen.
#  I've included an S class as an example (I'll generate the
#  others when I test your code) and it's __str__ output
#  should be "dot-dot-dot".
class Letter:
    def __init__(self, pattern=None):
        self.pattern = pattern

    # Second Version
    def __str__(self):
        response = []

        for symbol in self.pattern:
            if symbol == ".":
                response.append("dot")
            if symbol == "_":
                response.append("dash")

        return str("-".join(response))

class S(Letter):
    def __init__(self):
        pattern = ['.', '.', '.']
        super().__init__(pattern)

print(S())
# Bummer: Didn't get the right string output. Got: dot-dot-dot for `S()`
#                                       should be "dot-dot-dot".
    # First version
"""
    def __str__(self):
        response = []
        morse_code = list(self.pattern)
        counter = 0
        length = len(morse_code)
        for symbol in morse_code:
            if symbol == ".":
                response.append("dot")
            if symbol == "_":
                response.append("dash")
            if counter <= length-2:
                counter += 1
                response.append("-")
        return str("".join(response))
"""