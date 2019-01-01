#
#  Object-Oriented Python: Dice Roller
#  Python Techdegree
#
#  Created by Dulio Denis on 12/17/18.
#  Copyright (c) 2018 ddApps. All rights reserved.
# ------------------------------------------------
#  Challenge 1: Boards
# ------------------------------------------------
#  Challenge Task 1 of 2
#  Create a new Board subclass named TicTacToe. 
#  Have it automatically be a 3x3 board by automatically 
#  setting values in the __init__.
class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.cells = []
        for y in range(self.height):
            for x in range(self.width):
                self.cells.append((x, y))

    def __iter__(self):
        yield from self.cells

class TicTacToe(Board):
    def __init__(self):
        super().__init__(width=3, height=3)

ttt= TicTacToe()
print(ttt.cells)

#  Challenge Task 2 of 2
#  Now make all Board instances iterable so we can loop
#  through their cells attribute. If you need help, 
#  refer back to the Emulating Builtins video.
