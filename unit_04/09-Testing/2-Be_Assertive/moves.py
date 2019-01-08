class Move:
    better_than = None
    worse_than = None

    def __gt__(self, other):
        """Is this instance being compared to an instance from a worse class"""
        return other.__class__.__name__ in self.better_than

    def __lt__(self, other):
        """Is this instance being compared to an instance from a better class"""
        return other.__class__.__name__ in self.worse_than

    def __eq__(self, other):
        """Is this instance being compared to an instance from the same class"""
        return type(other) == type(self)

    def __ne__(self, other):
        """Is this instance being compared to an instance from another class"""
        return other.__class__ != self.__class__


class Rock(Move):
    better_than = ['Scissors']
    worse_than = ['Paper']


class Paper(Move):
    better_than = ['Rock']
    worse_than = ['Scissors']


class Scissors(Move):
    better_than = ['Paper']
    worse_than = ['Rock']