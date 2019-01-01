#
#  Object-Oriented Python: Advanced Objects
#  Python Techdegree
#
#  Created by Dulio Denis on 12/15/18.
#  Copyright (c) 2018 ddApps. All rights reserved.
# ------------------------------------------------
#  Filled List Class
# ------------------------------------------------
import copy

class FilledList(list):
    def __init__(self, count, value, *args, **kwargs):
        super().__init__() # just an empty list - ignore args & kwargs
        for _ in range(count):
            self.append(copy.copy(value))

filledList = FilledList(9, 2) # nine copies of the number 2
print(filledList)

filledList2 = FilledList(2, [0, 1])
print(filledList2)
filledList2[0][1] = 5
print(filledList2)

