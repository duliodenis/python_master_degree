#
#  Object-Oriented Python: Advanced Objects
#  Python Techdegree
#
#  Created by Dulio Denis on 12/15/18.
#  Copyright (c) 2018 ddApps. All rights reserved.
# ------------------------------------------------
#  JavaScript Object Class
#  use javascript dot "." notation to access a dictionary entry
# ------------------------------------------------
class JavaScriptObject(dict):
    def __getattribute__(self, item):
        try:
            return self[item]
        except KeyError:
            return super().__getattribute__(item)

jso = JavaScriptObject({"name": "Dulio"})
jso.language = "Python"
print(jso.name)
print(jso.language)
print(jso.fake_attribute)
