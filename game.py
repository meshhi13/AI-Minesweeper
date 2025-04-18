import pygame
from settings import *
from objects import *
import sys

def game_loop(rows, cols, mines):
    tilesize = WIDTH // cols
    board = Board(tilesize, rows, cols, mines)
    board.display()

    while True:
        clock.tick(FPS)        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                button = event.button
                board.handle_click(mouse_pos, button)

        screen.fill((0,0,255))
        board.draw(screen)
        
        if board.gameover:
            overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
            overlay.fill((0, 0, 0, 100)) 
            screen.blit(overlay, (0, 0))

            text = FONT.render("YOU WON!" if board.victory else "YOU LOST!", True, (255, 255, 255))
            text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
            screen.blit(text, text_rect)            

        pygame.display.flip()