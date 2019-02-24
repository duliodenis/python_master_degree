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

from typing import Union, Optional, List

from ingredient import Ingredient


class RecipeIngredient:
    def __init__(self, ingredient: Union[Ingredient, str], quantity: complex,
                 measurement: Optional[str]=None,
                 condition: Optional[str]=None):
        self.ingredient: Ingredient
        if isinstance(ingredient, Ingredient):
            self.ingredient = ingredient
        else:
            self.ingredient = Ingredient(ingredient)
        self.quantity: complex = quantity
        self.measurement: Optional[str] = measurement
        self.condition: Optional[str] = condition

    def __str__(self) -> str:
        condition: str = ''
        if self.condition:
            condition = f' ({self.condition})'
        amount: str
        if self.measurement:
            amount = f'{self.quantity} {self.measurement}'
        else:
            amount = self.quantity
        return f'{amount} {self.ingredient}{condition}'


class RecipeStep:
    def __init__(self, text: str):
        self.text: str = text

    def __str__(self) -> str:
        return self.text


class Recipe:
    def __init__(self, title: str):
        self.title: str = title
        self.ingredients: List[RecipeIngredient] = []
        self.steps: List[RecipeStep] = []

    def __str__(self) -> str:
        return (f'{self.title}: {len(self.ingredients)} ingredients, '
                f'{len(self.steps)} steps')

    def add_ingredient(self,
                       ingredient: Union[RecipeIngredient, Ingredient, str],
                       quantity: Optional[complex]=None,
                       measurement: Optional[str]=None,
                       condition: Optional[str]=None) -> None:
        if isinstance(ingredient, RecipeIngredient):
            self.ingredients.append(ingredient)
        else:
            assert quantity
            self.ingredients.append(
                RecipeIngredient(ingredient, quantity, measurement, condition)
            )

    def add_step(self, text: Union[RecipeStep, str], order :int=-1) -> None:
        if isinstance(text, RecipeStep):
            self.steps.insert(order, text)
        else:
            self.steps.insert(order, RecipeStep(text))

    def print(self) -> None:
        print(self.title)
        for ingredient in self.ingredients:
            print(ingredient)
        print('-'*20)
        for step in self.steps:
            print(step)

