#
#  Dates and Times in Python: Dates & Time
#  Python Techdegree
#
#  Created by Dulio Denis on 12/24/18.
#  Copyright (c) 2018 ddApps. All rights reserved.
# ------------------------------------------------
#  The Question Classes & the Plan
# ------------------------------------------------
class Question:
    answer = None
    text = None

class Add(Question):
    def __init__(self, num1, num2):
        self.text = "{} + {}".format(num1, num2)
        self.answer = num1 + num2

class Multiply(Question):
    def __init__(self, num1, num2):
        self.text = "{} x {}".format(num1, num2)
        self.answer = num1 * num2

# TEST
add1 = Add(5, 7)
print(add1.text)
print(add1.answer)
