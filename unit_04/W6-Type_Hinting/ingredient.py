#
#  Python Type Hinting: Generics 
#  Python Techdegree
#
#  Created by Dulio Denis on 2/24/19.
#  Copyright (c) 2019 ddApps. All rights reserved.
# ------------------------------------------------
#  Sometimes you can't specify your types just with
#  the built-in types. In that case, you can us
#  `Optional`, `Union`, and `List` from the `typing`
#  module to specify custom type combinations.

class Ingredient:
    def __init__(self, name: str):
        self.name: str = name

    def __str__(self) -> str:
        return self.name