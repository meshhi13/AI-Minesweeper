import pygame
import os
import sys

sys.setrecursionlimit(10**6)
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

VICTORY = False

WIDTH = 600
HEIGHT = 600
FPS = 60
TITLE = "Minesweeper AI"

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
pygame.display.set_caption(TITLE)
FONT = pygame.font.SysFont(pygame.font.get_default_font(), 50)


TEXT_COLOR = (255, 255, 255)

dirname = os.path.dirname(__file__)

def get_center(surface, x, y):
    center = (x - surface.get_width() // 2, y - surface.get_height() // 2)
    return center