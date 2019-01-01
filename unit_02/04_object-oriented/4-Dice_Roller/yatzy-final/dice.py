import random
from operator import attrgetter


class Die:
    template = """---------
|  {} {} {}  |
|  {} {} {}  |
|  {} {} {}  |
---------
"""
    pips = {
        1: [' ', ' ', ' ',
            ' ','*', ' ',
            ' ', ' ', ' '],
        2: ['*', ' ', ' ',
            ' ', ' ', ' ',
            ' ', ' ', '*'],
        3: ['*', ' ', ' ',
            ' ', '*', ' ',
            ' ', ' ', '*'],
        4: ['*', ' ', '*',
            ' ', ' ', ' ',
            '*', ' ', '*'],
        5: ['*', ' ', '*',
            ' ', '*', ' ',
            '*', ' ', '*'],
        6: ['*', ' ', '*',
            '*', ' ', '*',
            '*', ' ', '*']
    }

    MAX_ROLLS = 3

    def __init__(self, value=0):
        self.value = value or random.randint(1, 6)
        self.rolls = 1

    def reroll(self):
        if self.rolls == self.MAX_ROLLS:
            raise Exception('Can only roll a die 3 times')
        self.value = random.randint(1, 6)
        self.rolls += 1

    @property
    def can_be_rerolled(self):
        return self.rolls < self.MAX_ROLLS

    def __eq__(self, other):
        return self.value == other

    def __hash__(self):
        return id(self.value)

    def __repr__(self):
        return '<{}: {}>'.format(self.__class__.__name__, self.value)

    def __str__(self):
        return str(self.value)

    def __add__(self, other):
        return self.value + other

    def __radd__(self, other):
        return self.value + other

    @property
    def display(self):
        return self.template.format(*self.pips[self.value])


class Hand(list):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _ in range(5):
            self.append(Die())
        self[:] = list(sorted(self, key=attrgetter('value')))

        self.scorers = {
            'ones': self.score_ones,
            'twos': self.score_twos,
            'threes': self.score_threes,
            'fours': self.score_fours,
            'fives': self.score_fives,
            'sixes': self.score_sixes,
            'one_pair': self.score_one_pair,
            'two_pairs': self.score_two_pairs,
            'three_of_a_kind': self.score_three_of_a_kind,
            'four_of_a_kind': self.score_four_of_a_kind,
            'small_straight': self.score_small_straight,
            'large_straight': self.score_large_straight,
            'full_house': self.score_full_house,
            'chance': self.score_chance,
            'yatzy': self.score_yatzy,
        }

    def _by_value(self, value):
        dice = []
        for die in self:
            if die.value == value:
                dice.append(die)
        return dice

    @property
    def _sets(self):
        return {
            1: len(self.ones),
            2: len(self.twos),
            3: len(self.threes),
            4: len(self.fours),
            5: len(self.fives),
            6: len(self.sixes)
        }

    def _by_count(self, count):
        dice = []
        for num, total in self._sets.items():
            if total == count:
                dice.append(num)
        return dice

    @property
    def _of_a_kind(self):
        return {
            1: self._by_count(1),
            2: self._by_count(2),
            3: self._by_count(3),
            4: self._by_count(4),
            5: self._by_count(5)
        }

    @property
    def ones(self):
        return self._by_value(1)

    @property
    def twos(self):
        return self._by_value(2)

    @property
    def threes(self):
        return self._by_value(3)

    @property
    def fours(self):
        return self._by_value(4)

    @property
    def fives(self):
        return self._by_value(5)

    @property
    def sixes(self):
        return self._by_value(6)

    def score_ones(self):
        return sum(self.ones)

    def score_twos(self):
        return sum(self.twos)

    def score_threes(self):
        return sum(self.threes)

    def score_fours(self):
        return sum(self.fours)

    def score_fives(self):
        return sum(self.fives)

    def score_sixes(self):
        return sum(self.sixes)

    def _score_set(self, num):
        scores = [0] * num

        for value, count in self._sets.items():
            if count == num:
                scores.append(value*num)

        tops = []
        for _ in range(num):
            top_score = max(scores)
            scores.remove(top_score)
            tops.append(top_score)

        return sum(tops)

    def score_one_pair(self):
        score = [0]

        for value, count in self._sets.items():
            if count == 2:
                score.append(value*2)

        return max(score)

    def score_two_pairs(self):
        return self._score_set(2)

    def score_three_of_a_kind(self):
        return self._score_set(3)

    def score_four_of_a_kind(self):
        return self._score_set(4)

    def score_yatzy(self):
        if self._of_a_kind[5]:
            return 50
        return 0

    def score_chance(self):
        return sum(self)

    def score_small_straight(self):
        if all([self._sets[1] == 1, self._sets[2] == 1, self._sets[3] == 1,
                self._sets[4] == 1, self._sets[5] == 1]):
            return 15
        return 0

    def score_large_straight(self):
        if all([self._sets[2] == 1, self._sets[3] == 1,self._sets[4] == 1,
                self._sets[5] == 1, self._sets[6] == 1]):
            return 20
        return 0

    def score_full_house(self):
        try:
            two = max(self._of_a_kind[2])
            three = max(self._of_a_kind[3])
        except ValueError:
            return 0
        else:
            if two and three:
                return (two * 2) + (three * 3)

    def score_max(self, limit=None):
        scores = {
            'ones': self.score_ones(),
            'twos': self.score_twos(),
            'threes': self.score_threes(),
            'fours': self.score_fours(),
            'fives': self.score_fives(),
            'sixes': self.score_sixes(),
            'one_pair': self.score_one_pair(),
            'two_pairs': self.score_two_pairs(),
            'three_of_a_kind': self.score_three_of_a_kind(),
            'four_of_a_kind': self.score_four_of_a_kind(),
            'small_straight': self.score_small_straight(),
            'large_straight': self.score_large_straight(),
            'full_house': self.score_full_house(),
            'chance': self.score_chance(),
            'yatzy': self.score_yatzy()
        }
        if limit:
            for key in scores.copy():
                if key not in limit:
                    del scores[key]
        return max(scores, key=scores.get)

    def __str__(self):
        return ', '.join([str(die) for die in self])

    def score(self, what):
        return self.scorers[what]()

    def display(self, width=0, show_key=False):
        die_lines = []
        for die in self:
            die_lines.append(die.display.split('\n'))
        for i in range(5):
            for die in die_lines:
                print('{0:^{1}}'.format(die[i], width//5), end='')
            print('')
        if show_key:
            for num in range(1, 6):
                if self[num-1].can_be_rerolled:
                    print('{0:^{1}}'.format('[{}]'.format(num), width//5), end='')
                else:
                    print('{0:^{1}}'.format('', width//5), end='')
            print('')

    @property
    def left_to_reroll(self):
        return any([die.can_be_rerolled for die in self])
