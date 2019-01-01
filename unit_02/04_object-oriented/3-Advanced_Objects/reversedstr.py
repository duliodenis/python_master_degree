#
#  Object-Oriented Python: Advanced Objects
#  Python Techdegree
#
#  Created by Dulio Denis on 12/15/18.
#  Copyright (c) 2018 ddApps. All rights reserved.
# ------------------------------------------------
#  Reversed String Class
# ------------------------------------------------
class ReversedStr(str):
    def __new__(*args, **kwargs):
        self = str.__new__(*args, **kwargs)
        self = self[::-1]
        return self

print(ReversedStr("hello"))