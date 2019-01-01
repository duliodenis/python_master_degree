#
#  Dungeon Game: Movement
#  Python Techdegree
#
#  Created by Dulio Denis on 12/12/18.
#  Copyright (c) 2018 ddApps. All rights reserved.
# ------------------------------------------------
#  Challenge Task 1 of 1
#  Our game's player only has two attributes, x and y coordinates. 
#  Let's practice with a slightly different one, though. 
#  This one has x, y, and "hp", which stands for hit points.
#  Our move function takes this three-part tuple player and a direction tuple that's two parts, 
#  the x to move and the y (like (-1, 0) would move to the left but not up or down).
#  Finish the function so that if the player is being run into a wall, their hp is reduced by 5. 
#  Don't let them go past the wall. Consider the grid to be 0-9 in both directions. 
#  Don't worry about keeping their hp above 0 either.
#  EXAMPLES:
#  move((1, 1, 10), (-1, 0)) => (0, 1, 10)
#  move((0, 1, 10), (-1, 0)) => (0, 1, 5)
#  move((0, 9, 5), (0, 1)) => (0, 9, 0)

def move(player, direction):
    x, y, hp = player

    if direction == (-1,0):
        x -= 1
        if x < 0:
            hp -= 5
            x += 1
    elif direction == (1,0):
        x += 1
        if x > 9:
            hp -= 5
            x -= 1
    elif direction == (0,-1):
        y -= 1
        if y < 0:
            hp -= 5
            y += 1
    elif direction == (0,1):
        y += 1
        if y > 9:
            hp -= 5
            y -=1

    return x, y, hp

print(move((1, 1, 10), (-1, 0)))
print(move((0, 1, 10), (-1, 0)))
print(move((0, 9, 5), (0, 1)))
