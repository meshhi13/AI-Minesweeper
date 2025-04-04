import pygame
from settings import *
import sys

class Menu():
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()

    def run(self):
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()

    def draw(self):
        self.screen.fill(126, 144, 234)
    
    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
