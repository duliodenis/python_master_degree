#
#  Dungeon Game
#  Python Techdegree
#
#  Created by Dulio Denis on 12/12/18.
#  Copyright (c) 2018 ddApps. All rights reserved.
# ------------------------------------------------
#  Create a game with a 2-dimensional map. 
#  Place the player, a door, and a monster into random spots in your map. 
#  Let the player move around in the map and, after each move, tell them if they've found the door or the monster. 
#  If they find either the game is over. The door is the win condition, the monster is the lose condition.
#  
import random
import os

# Outline
# -----------
# draw the grid
# pick random location for player
# pick random location for exit door
# pick random location for monster
# draw player in the grid
# take input for movement
# move player, unless invalid move (past edges of grid)
# check for win/loss
# clear screen and redraw grid

# List of tuples
CELLS = [(0,0), (1,0), (2,0), (3,0), (4,0),
         (0,1), (1,1), (2,1), (3,1), (4,1),
         (0,2), (1,2), (2,2), (3,2), (4,2),
         (0,3), (1,3), (2,3), (3,3), (4,3),
         (0,4), (1,4), (2,4), (3,4), (4,4)]

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_locations():
    # monster = None
    # door = None
    # player = None
    # return monster, door, player
    return random.sample(CELLS, 3)


def move_player(player, move):
    x, y = player
    if move == "LEFT":
        x -= 1
    if move == "RIGHT":
        x += 1
    if move == "UP":
        y -= 1
    if move == "DOWN":
        y += 1
    # get the player's location
    # if move == LEFT,  x-1
    # if move == RIGHT, x+1
    # if move == UP,    y-1
    # if move == DOWN,  y+1
    # return player
    return x, y

def get_moves(player):
    moves = ["LEFT", "RIGHT", "UP", "DOWN"]
    x, y = player
    # if player's y == 0, they can't move UP
    # if player's y == 4, they can't move DOWN
    # if player's x == 0, they can't move LEFT
    # if player's x == 4, they can't move RIGHT
    if x == 0:
        moves.remove("LEFT")
    if x == 4:
        moves.remove("RIGHT")
    if y == 0:
        moves.remove("UP")
    if y == 4:
        moves.remove("DOWN")
    return moves

def draw_map(player):
    print(" _" * 5)
    tile = "|{}"
    for cell in CELLS:
        x, y = cell
        if x < 4:
            line_end = ""
            if cell == player:
                output = tile.format("X")
            else:
                output = tile.format("_")
        else:
            line_end = "\n"
            if cell == player:
                output = tile.format("X|")
            else:
                output = tile.format("_|")
        print(output, end=line_end)

def game_loop():
    monster, door, player = get_locations()
    playing = True

    while playing:
        clear_screen()
        draw_map(player)
        valid_moves = get_moves(player)
        print("You're currently in room {}".format(player)) # fill in with player position
        print("You can move {}".format(", ".join(valid_moves))) # fill with available moves
        print("Enter Q to Quit")

        move = input("> ").upper()
        if move == 'Q':
            print("\n ** See you next time. **\n")
            break
        if move in valid_moves:
            player = move_player(player, move)

            if player == monster:
                print("\n ** Oh no! The monster got you. Better luck next time! **\n")
                playing = False

            if player == door:
                print("\n ** You've escaped! Congratulations! **\n")
                playing = False

        else:
            input("\n ** Walls are hard! Don't run into them! **\n")
    else:
        if input("Play again? [Y/n] ").lower() != 'n':
            game_loop()

        # Good move? Change the player position.
        # Bad move? Don't change anything!
        # On the door? They win!
        # On the monster? They lose!
        # Otherwise, loop back around.

clear_screen()
print("Welcome to the dungeon!")
input("Press RETURN to START")
clear_screen()
game_loop()
