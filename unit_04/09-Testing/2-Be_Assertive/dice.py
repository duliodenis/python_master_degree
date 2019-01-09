import random
import re

die_pattern = re.compile(r'^(?P<num>\d+)d(?P<sides>\d+)$', re.I)


class Die:
    value = None

    def __init__(self, sides=6):
        try:
            assert sides >= 2
        except AssertionError:
            raise ValueError("Die needs at least 2 sides")
        else:
            self.sides = sides
        self.value = self.roll()

    def roll(self):
        return random.randint(1, self.sides)

    def __int__(self):
        return self.value

    def __repr__(self):
        return str(self.value)

    def __add__(self, other):
        return int(self) + other

    def __radd__(self, other):
        return int(self) + other

    def __eq__(self, other):
        return all([
            self.sides == other.sides,
            self.value == other.value
        ])


class Roll:
    def __init__(self, description="1d6"):
        self.results = []

        try:
            num, sides = die_pattern.match(description).groups()
        except AttributeError:
            raise ValueError("Your description should be in the format '1d6'.")
        else:
            num = int(num)
            sides = int(sides)

            for _ in range(num):
                self.results.append(Die(sides))

    def __int__(self):
        return sum(self.results)

    def __repr__(self):
        return str(int(self))

    def __add__(self, other):
        return int(self) + other

    def __radd__(self, other):
        return int(self) + other

    def __contains__(self, item):
        return any([item == die for die in self.results])

    def __getitem__(self, index):
        try:
            return self.results[index]
        except IndexError as err:
            raise err