#
#  Number Guessing Game
#  Python Techdegree
#
#  Created by Dulio Denis on 2/7/17.
#  Copyright (c) 2017 ddApps. All rights reserved.
# ------------------------------------------------
#  Guess what number the computer picked.
#  The computer tells you if your guess is too low or high.
# ------------------------------------------------
# v1: basic functionality
# v2: limit the number of guesses, catch non-integer submissions,
#     print too low or too high messages for bad guesses,
#     let people play again
#
import random

def game():
    # generate a random number between 1 and 10
    secret_num = random.randint(1, 10)

    # we'll give the player 5 tries
    tries = 5

    # set up the game loop
    while tries > 0:
        # get a number guess from the player
        # use try / except to catch non-integer guesses
        try:
            guess = int(input("Guess a number between 1 and 10. I'll give you {} tries: ".format(tries)))
        except ValueError:
            print("You must enter an integer value as a guess.")
            continue

        # compare guess to the secret number
        if guess == secret_num:
            print("You got it! My number was {}".format(secret_num))
            break
        else:
            tries -= 1
            if tries == 0:
                print("Better luck next time.")

            else:
                # print too low or too high
                if guess > secret_num:
                    print("Too high.")
                else:
                    print("Too low.")
                print("Try again. You have {} tries left".format(tries))
    else:
        print("You didn't get it. My number was {}.".format(secret_num))
    play_again = input("Do you want to play again? Y/n ")
    if play_again.lower() != 'n':
        game()
    else:
        print("Thanks for playing.")

game()
