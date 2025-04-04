import pygame
import os

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (40, 40, 40)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
BGCOLOR = RED

TILESIZE = 32
ROWS = 15
COLS = 15
AMOUNT_MINES = 5
WIDTH = TILESIZE * ROWS
HEIGHT = TILESIZE * ROWS
FPS = 60
TITLE = "Minesweeper AI"

tilenumbers = []
dirname = os.path.dirname(__file__)

for i in range(1, 9):
    tilenumbers.append(pygame.transform.scale(pygame.image.load(os.path.join(dirname, f"Assets\Tile{i}.png")), (TILESIZE, TILESIZE)))

tileempty = pygame.transform.scale(pygame.image.load(os.path.join(dirname, "Assets\TileEmpty.png")), (TILESIZE, TILESIZE))
tileexploded = pygame.transform.scale(pygame.image.load(os.path.join(dirname, "Assets\TileExploded.png")), (TILESIZE, TILESIZE))
tileflag = pygame.transform.scale(pygame.image.load(os.path.join(dirname, "Assets\TileFlag.png")), (TILESIZE, TILESIZE))
tilemine = pygame.transform.scale(pygame.image.load(os.path.join(dirname, "Assets\TileMine.png")), (TILESIZE, TILESIZE))
tilenotmine = pygame.transform.scale(pygame.image.load(os.path.join(dirname, "Assets\TileNotMine.png")), (TILESIZE, TILESIZE))
tileunknown = pygame.transform.scale(pygame.image.load(os.path.join(dirname, "Assets\TileUnknown.png")), (TILESIZE, TILESIZE))