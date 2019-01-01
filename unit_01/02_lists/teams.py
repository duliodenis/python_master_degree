#
#  Teams
#  Python Techdegree
#
#  Created by Dulio Denis on 12/1/18.
#  Copyright (c) 2018 ddApps. All rights reserved.
# ------------------------------------------------
#  List Creation Challenge
#  Add Players to a team and select a goalie.
#
# TODO Create an empty list to maintain the player names
players = []

# TODO Ask the user if they'd like to add players to the list.
add_player = input("Would you like to add players to the list? (Yes/No):  ")
# If the user answers "Yes", let them type in a name and add it to the list.
while add_player.lower() == 'yes':
  new_player = input("Enter the name of the player to add to the team: ")
  players.append(new_player)
  add_player = input("Would you like to add another players to the list? (Yes/No):  ")

# If the user answers "No", print out the team 'roster'
else:
  counter = 1
  for player in players:
    count = str(counter)
    print("Player {}: {}".format(counter, player))
    counter += 1

# TODO print the number of players on the team
print("There are {} players on the team".format(len(players)))

# TODO Print the player number and the player name
# The player number should start at the number one


# TODO Select a goalkeeper from the above roster
goalie = input("Please select the goal keeper by selecting the player number. (1 - {}) ".format( len(players)))

# TODO Print the goal keeper's name
# Remember that lists use a zero based index
print("Great! The goalkeeper for the game will be", players[int(goalie) - 1])