import random

import dice

BOT_NAMES = [
    'Acid Burn',
    'Crash Override',
    'Zero Cool',
    'Cereal Killer',
    'Lord Nikon',
    'The Plague',
    'Razor',
    'Blade',
    'Phantom Phreak',
]


class Category:
    def __init__(self, name, display, key, score=None):
        self.name = name
        self.display = display
        self.key = key
        self.score = score

    def __str__(self):
        return self.display

    def __add__(self, other):
        return self.score + other

    def __radd__(self, other):
        return self.score + other


class Scoresheet:
    def __init__(self):
        self.categories = (
            Category('ones', 'Ones', '1'),
            Category('twos', 'Twos', '2'),
            Category('threes', 'Threes', '3'),
            Category('fours', 'Fours', '4'),
            Category('fives', 'Fives', '5'),
            Category('sixes', 'Sixes', '6'),
            Category('one_pair', 'One Pair', 'O'),
            Category('two_pairs', 'Two Pairs', 'T'),
            Category('three_of_a_kind', 'Three of a Kind', 'K'),
            Category('four_of_a_kind', 'Four of a Kind', 'F'),
            Category('small_straight', 'Small Straight', 'S'),
            Category('large_straight', 'Large Straight', 'L'),
            Category('full_house', 'Full House', 'H'),
            Category('chance', 'Chance', 'C'),
            Category('yatzy', 'Yatzy', 'Y'),
        )

    def __getitem__(self, item):
        try:
            return [category for category in self.categories if category.name == item][0]
        except IndexError:
            raise KeyError

    def get_by_key(self, key):
        try:
            return [category for category in self.categories if category.key == key][0]
        except IndexError:
            raise KeyError

    @property
    def score(self):
        return sum([score for score in self.categories if score.score is not None])

    @property
    def open_categories(self):
        categories = []
        for category in self.categories:
            if category.score is None:
                categories.append(category)
        return categories

    @property
    def open_keys(self):
        keys = []
        for category in self.categories:
            if category.score is None:
                keys.append(category.key)
        return keys

    def display(self, width):
        for index, category in enumerate(self.open_categories, start=1):
            print("{0:^{1}}".format(
                '{} [{}]'.format(category.display, category.key),
                width//3
            ), end='\t')
            if not index % 3:
                print('')
        print('')

    def score_category(self, key, score):
        try:
            category = [category for category in self.categories if category.key == key][0]
        except IndexError:
            raise KeyError
        category.score = score



class Player:
    def __init__(self, order):
        self.order = order
        self.scoresheet = Scoresheet()
        self.hand = None

    def __repr__(self):
        return '<{}: {}>'.format(self.__class__.__name__, str(self))

    def roll(self):
        self.hand = dice.Hand()
        return

    @property
    def score(self):
        return self.scoresheet.score


class Human(Player):
    def __init__(self, order, name=None):
        super().__init__(order)
        self.name = name

    def __str__(self):
        return self.name

    def show_available_scores(self):
        print(
            "You can score: {}".format(
                ', '.join(
                    self.scoresheet.open_categories
                )
            )
        )

    def get_score(self):
        what_to_score = input("What do you want to score? ")
        if what_to_score not in self.scoresheet.open_categories:
            return self.get_score()
        score = self.hand.score(what_to_score)
        self.scoresheet[what_to_score] = score
        return

    def play_round(self):
        super().play_round()

    # def play_round(self):
    #     super().play_round()
    #     # print('{:^90}'.format(self.hand.display()))
    #     print('\n', '-'*90)
    #     self.get_score()
    #     return


class Bot(Player):
    def __init__(self, order):
        super().__init__(order)
        self.name = random.choice(BOT_NAMES)

    def __str__(self):
        return self.name

    def __eq__(self, other):
        return self.name == other.name

    def __hash__(self):
        return id(str(self.name))

    def play_round(self):
        super().play_round()
        best_move = self.hand.score_max(self.scoresheet.open_categories)
        score = self.hand.score(best_move)
        self.scoresheet[best_move] = score
        return

