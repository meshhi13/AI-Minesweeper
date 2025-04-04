import pygame
from settings import *
import random

# "0" unknown
# "1" mine
# "2" clue
# "3" empty

class Tile:
    def __init__(self, x, y, image, type, revealed=False, flagged=False):
        self.x, self.y = TILESIZE * x, TILESIZE * y
        self.image = image
        self.type = type
        self.revealed = revealed
        self.flagged = flagged


    def draw(self, board_surface):
        board_surface.blit(self.image, (self.x, self.y))

    def __repr__(self):
        return self.type

class Board:
    def __init__(self):
        self.board_surface = pygame.Surface((WIDTH, HEIGHT))
        self.board_list = [[Tile(col, row, tileempty, "0") for row in range(ROWS)] for col in range(COLS)]
        self.place_mines()

    def place_mines(self):
        for tile in range(AMOUNT_MINES):
            while True:
                x_pos = random.randint(0, ROWS-1)
                y_pos = random.randint(0, COLS-1)

                if self.board_list[x_pos][y_pos].type == "0":
                    self.board_list[x_pos][y_pos].image = tilemine
                    self.board_list[x_pos][y_pos].type = "1"
                    break

    def draw(self, screen):
        for row in self.board_list:
            for tile in row:
                tile.draw(self.board_surface)
        screen.blit(self.board_surface, (0, 0))

    def display(self):
        for row in self.board_list:
            print(row)    