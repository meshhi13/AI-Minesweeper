from itertools import cycle

SIZES = cycle([10, 15, 20, 25, 30, 35, 40])
MINES = cycle([15, 35, 60, 95, 135, 200, 280])

class GameState:
    def __init__(self):
        self.rows = 10
        self.cols = 10
        self.mines = 15