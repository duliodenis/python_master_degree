#
#  Object-Oriented Python: Inheritance Characters
#  Python Techdegree
#
#  Created by Dulio Denis on 12/13/18.
#  Copyright (c) 2018 ddApps. All rights reserved.
# ------------------------------------------------
#  Classes are great, but they're even better with parents.
import random

class Character:
    def __init__(self, name, **kwargs):
        self.name = name
        for attribute, value in kwargs.items():
            setattr(self, attribute, value)

class Thief(Character):
    sneaky = True

    def __init__(self, name, **kwargs):
        # a way to make use of the code that lives in our classes' superclasses.
        super().__init__(name, **kwargs)
        self.sneaky = True

    def pickpocket(self):
        return self.sneaky and bool(random.randint(0, 1))

    def hidie(self, light_level):
        return self.sneaky and light_level < 10

kenneth = Thief("Kenneth")
print(kenneth.name)
print(kenneth.sneaky)
