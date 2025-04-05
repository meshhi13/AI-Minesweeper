import pygame
from settings import *
import sys
from text_input import *

class Menu():
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()

    def getScreen(self):
        return self.screen

    def drawtext(self, text, x, y, font):
        img = font.render(text, True, TEXT_COLOR)
        self.screen.blit(img,  get_center(img, x, y))

    def run(self):
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)    
            self.events() 
            self.draw()

    def draw(self):
        self.screen.fill(SKYBLUE)
        self.drawtext("MINESWEEPER AI", WIDTH/2, HEIGHT/4, FONT)
        input_box1 = InputBox(100, 100, 140, 32)
        input_box2 = InputBox(100, 300, 140, 32)
        self.input_boxes = [input_box1, input_box2]
        pygame.display.flip()
    
    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            for box in self.input_boxes:
                box.handle_event(event)

menu = Menu()

while True:
    menu.run()
