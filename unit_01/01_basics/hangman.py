#
#  Hangman
#  Python Techdegree
#
#  Created by Dulio Denis on 2/9/17.
#  Copyright (c) 2017 ddApps. All rights reserved.
# ------------------------------------------------
#  Guess what word the computer picked.
#
import random
import os
import sys

# make a list of words
words = [
    'apple',
    'banana',
    'orange',
    'coconut',
    'strawberry',
    'lime',
    'grapefruit',
    'lemon',
    'kumquat',
    'pineapple',
    'blueberry',
    'melon'
]

# clear the screen
def clear():
    # if windows
    if os.name == 'nt':
        os.system('cls')
    # else its Unix based like macOS and Linux
    else:
        os.system('clear')


# draw function
def draw(bad_guesses, good_guesses, secret_word):
    # clear the screen first
    clear()
    # and draw the strikes
    print('Strikes: {}/7'.format(len(bad_guesses)))
    print('') # a blank line just for formatting

    # draw the bad guesses
    for letter in bad_guesses:
        print(letter, end = ' ')
    print('\n\n')

    # then draw guessed letters
    for letter in secret_word:
        if letter in good_guesses:
            print(letter, end=' ')
        else:
            print('_', end=' ')


# get the guess
def get_guess(bad_guesses, good_guesses):
    while True:
        # take a guess and lowercase it right away
        guess = input("Guess a letter: ").lower()

        # validate its a legitimate guess
        if (len(guess)) != 1:
            print("You can only guess a single letter")
        elif guess in bad_guesses or guess in good_guesses:
            print("You've already guessed that letter.")
        elif not guess.isalpha():
            print("You can only guess letters.")
        else:
            return guess


# play the game
def play(done):
    # clear the screen
    clear()
    # pick a random word
    secret_word = random.choice(words)

    # have both a good and bad guess letter list
    bad_guesses = []
    good_guesses = []

    while True:
        draw(bad_guesses, good_guesses, secret_word)
        guess = get_guess(bad_guesses, good_guesses)

        if guess in secret_word:
            good_guesses.append(guess)
            found = True
            for letter in secret_word:
                if letter not in good_guesses:
                    found = False
            if found:
                print("You win!")
                print("The secret word was {}".format(secret_word))
                done = True
        else:
            bad_guesses.append(guess)
            if len(bad_guesses) == 7:
                draw(bad_guesses, good_guesses, secret_word)
                print("You lost!")
                print("The secret word was {}".format(secret_word))
                done = True
        if done:
            play_again = input('Play again? Y/n ').lower()
            if play_again != 'n':
                return play(done=False)
            else:
                sys.exit()


def welcome():
    print('Welcome to Hangman!')
    start = input('Press enter/return to start or Q to quit ').lower()
    if start == 'q':
        print('Thanks for playing.')
        sys.exit()
    else:
        return True

done = False
while True:
    clear()
    welcome()
    play(done)
