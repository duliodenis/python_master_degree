#
#  Vending Machine
#  Python Techdegree
#
#  Created by Dulio Denis on 12/8/18.
#  Copyright (c) 2018 ddApps. All rights reserved.
# ------------------------------------------------
#  Holding onto the items we remove from a list with
#  the .pop() method makes this super easy!
#
sodas = ["Pepsi", "Cherry Coke Zero", "Sprite"]
chips = ["Doritos", "Fritos"]
candy = ["Snickers", "M&Ms", "Twizzlers"]

while True:
    choice = input("Would you like a SODA, CHIPS, or CANDY? ").lower()
    try:
        if choice == "soda":
            snack = sodas.pop()
        elif choice == "chips":
            snack = chips.pop()
        elif choice == "candy":
            snack = candy.pop()
        else:
            print("Sorry, I didn't understand the choice.")
            continue
    except IndexError:
        print("We're all out of {}. Try another selection.".format(choice))
        continue
    print("Here is your {}: {}".format(choice, snack))
