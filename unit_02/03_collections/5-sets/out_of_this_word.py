#
#  Out of this Word Game
#  Python Techdegree
#
#  Created by Dulio Denis on 12/11/18.
#  Copyright (c) 2018 ddApps. All rights reserved.
# ------------------------------------------------
#  A quick word game using the set features you've just picked up.
import random

WORDS = (
    "treehouse",
    "python",
    "learner",
)

def prompt_for_words(challenge):
    guesses = set()
    print("What words can you find in the word '{}'".format(challenge))
    print("(Enter Q to Quit)")
    while True:
        guess = input("{} words >  ".format(len(guesses)))
        if guess.upper() == "Q":
            break
        guesses.add(guess.lower())
    return guesses

def output_results(results):
    for word in results:
        print("* " + word)

challenge_word = random.choice(WORDS)

player_1_words = prompt_for_words(challenge_word)
player_2_words = prompt_for_words(challenge_word)

print("Player 1 Results:")
player_1_unique = player_1_words - player_2_words
print("{} guesses, {} unique".format(len(player_1_words), len(player_1_unique)))
output_results(player_1_unique)
print("-" * 20)

print("Player 2 Results:")
player_2_unique = player_2_words - player_1_words
print("{} guesses, {} unique".format(len(player_2_words), len(player_2_unique)))
output_results(player_2_unique)
print("-" * 20)

print("Shared Guesses:")
shared_words = player_1_words & player_2_words
output_results(shared_words)