from operator import attrgetter
from test.support import captured_stdout, captured_stdin
import unittest

import yatzy
import player
import dice

player_scores = {
    'ones': None,
    'twos': None,
    'threes': None,
    'fours': None,
    'fives': None,
    'sixes': None,
    'one_pair': None,
    'two_pairs': None,
    'three_of_a_kind': None,
    'four_of_a_kind': None,
    'small_straight': None,
    'large_straight': None,
    'full_house': None,
    'chance': None,
    'yatzy': None
}


class GameTests(unittest.TestCase):
    def test_bad_init(self):
        with self.assertRaises(ValueError):
            game = yatzy.Yatzy()

    def test_one_human(self):
        with captured_stdout() as stdout, captured_stdin() as stdin:
            stdin.write("Kenneth")
            stdin.seek(0)
            game = yatzy.Yatzy(humans=1)
        self.assertEqual("Name for Player 1: ", stdout.getvalue())
        self.assertEqual(len(game.humans), 1)

    def test_two_humans(self):
        with captured_stdout() as stdout, captured_stdin() as stdin:
            stdin.write("Kenneth\n")
            stdin.write("Elaine\n")
            stdin.seek(0)
            game = yatzy.Yatzy(humans=2)
        self.assertIn("Name for Player 2:", stdout.getvalue())
        self.assertEqual(len(game.humans), 2)
        self.assertEqual(game.humans[1].name, "Elaine")

    def test_one_bot(self):
        game = yatzy.Yatzy(bots=1)
        self.assertEqual(len(game.bots), 1)

    def test_two_bots(self):
        game = yatzy.Yatzy(bots=2)
        self.assertEqual(len(game.bots), 2)
        self.assertEqual(len({game.bots[0].name, game.bots[1].name}), 2)

    def test_player_display(self):
        with captured_stdout() as stdout, captured_stdin() as stdin:
            stdin.write("Kenneth\n")
            stdin.seek(0)
            game = yatzy.Yatzy(humans=1)
            stdout.seek(0)
            game.show_player_info(game.humans[0])
        output = stdout.getvalue()
        self.assertEqual(len(output.split('\n')[0]), 90)
        self.assertIn(game.humans[0].name, output)


class PlayerTests(unittest.TestCase):
    def test_human(self):
        human1 = player.Human(1, "Kenneth")
        self.assertEqual(human1.name, "Kenneth")

    def test_bot(self):
        bot1 = player.Bot(1)
        self.assertIn(bot1.name, player.BOT_NAMES)

    def test_score_sorting(self):
        human1 = player.Human(1, "Kenneth")
        human2 = player.Human(1, "Elaine")
        for category in player_scores:
            human1.scoresheet[category].score = 1
            human2.scoresheet[category].score = 5
        self.assertGreater(human2.score, human1.score)


class DiceTests(unittest.TestCase):
    def test_die(self):
        die = dice.Die()
        self.assertIn(die, range(1, 7))
        self.assertEqual(die.rolls, 1)

    def test_die_value(self):
        die = dice.Die(8)
        self.assertEqual(die.value, 8)

    def test_reroll(self):
        die = dice.Die()
        die.reroll()
        self.assertEqual(die.rolls, 2)

    def test_roll_limit(self):
        die = dice.Die()
        die.rolls = 3

        with self.assertRaises(Exception):
            die.reroll()


class HandTests(unittest.TestCase):
    def setUp(self):
        self.dice = [dice.Die(n) for n in range(1, 7)]

    def _seed(self, nums):
        return [dice.Die(num) for num in nums]

    def test_hand(self):
        hand = dice.Hand()
        self.assertEqual(len(hand), 5)

    def test_ones(self):
        hand = dice.Hand()
        hand[:] = self.dice[:5]
        self.assertEqual(hand.score_ones(), 1)

    def test_twos(self):
        hand = dice.Hand()
        hand[:] = self.dice[:5]
        self.assertEqual(hand.score_twos(), 2)

    def test_threes(self):
        hand = dice.Hand()
        hand[:] = self.dice[:5]
        self.assertEqual(hand.score_threes(), 3)

    def test_fours(self):
        hand = dice.Hand()
        hand[:] = self.dice[:5]
        self.assertEqual(hand.score_fours(), 4)

    def test_fives(self):
        hand = dice.Hand()
        hand[:] = self.dice[:5]
        self.assertEqual(hand.score_fives(), 5)

    def test_sixes(self):
        hand = dice.Hand()
        hand[:] = self.dice[1:]
        self.assertEqual(hand.score_sixes(), 6)

    def test_one_pair(self):
        hand = dice.Hand()
        hand[:] = [self.dice[0], self.dice[0], self.dice[3]]
        self.assertEqual(hand.score_one_pair(), 2)

    def test_one_pair_no_pairs(self):
        hand = dice.Hand()
        hand[:] = self.dice[:5]
        self.assertEqual(hand.score_one_pair(), 0)

    def test_two_pairs(self):
        hand = dice.Hand()
        hand[:] = [self.dice[0], self.dice[0], self.dice[3], self.dice[3]]
        self.assertEqual(hand.score_two_pairs(), 10)

    def test_two_pairs_no_pairs(self):
        hand = dice.Hand()
        hand[:] = self.dice[1:]
        self.assertEqual(hand.score_two_pairs(), 0)

    def test_two_pairs_one_pair(self):
        hand = dice.Hand()
        hand[:] = [self.dice[0], self.dice[0], self.dice[3]]
        self.assertEqual(hand.score_two_pairs(), 2)

    def test_three_of_a_kind(self):
        hand = dice.Hand()
        hand[:] = self._seed([2, 2, 2, 4, 5])
        self.assertEqual(hand.score_three_of_a_kind(), 6)

    def test_four_of_a_kind(self):
        hand = dice.Hand()
        hand[:] = self._seed([2, 2, 2, 2, 5])
        self.assertEqual(hand.score_four_of_a_kind(), 8)

    def test_yatzy(self):
        hand = dice.Hand()
        hand[:] = self._seed([2, 2, 2, 2, 2])
        self.assertEqual(hand.score_yatzy(), 50)

    def test_small_straight(self):
        hand = dice.Hand()
        hand[:] = self.dice[:5]
        self.assertEqual(hand.score_small_straight(), 15)

    def test_large_straight(self):
        hand = dice.Hand()
        hand[:] = self.dice[1:]
        self.assertEqual(hand.score_large_straight(), 20)

    def test_full_house(self):
        hand = dice.Hand()
        hand[:] = self._seed([1, 1, 1, 5, 5])
        self.assertEqual(hand.score_full_house(), 13)

    def test_chance(self):
        hand = dice.Hand()
        hand[:] = self._seed([4, 3, 3, 2, 1])
        self.assertEqual(hand.score_chance(), 13)

    def test_max_score(self):
        hand = dice.Hand()
        hand[:] = self._seed([2, 2, 5, 5, 5])
        self.assertEqual(hand.score_max(), 'full_house')
