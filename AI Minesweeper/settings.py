import pygame
import os

pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (40, 40, 40)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
OFFBLUE = (23, 61, 252)
SKYBLUE = (126, 144, 234)
BGCOLOR = SKYBLUE
COLOR_INACTIVE = GREY
COLOR_ACTIVE = OFFBLUE

TILESIZE = 32
ROWS = 15
COLS = 15
AMOUNT_MINES = 5
WIDTH = TILESIZE * ROWS
HEIGHT = TILESIZE * ROWS
FPS = 60
TITLE = "Minesweeper AI"

FONT = pygame.font.SysFont(pygame.font.get_default_font(), 50)
TEXT_COLOR = (255, 255, 255)

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

def get_center(surface, x, y):
    center = (x - surface.get_width() // 2, y - surface.get_height() // 2)
    return center