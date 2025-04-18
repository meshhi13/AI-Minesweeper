import pygame
from settings import *
from objects import *
import sys

def game_loop(rows, cols, mines):
    tilesize = WIDTH // cols
    board = Board(tilesize, rows, cols, mines)
    board.display()
    text_highlight = False

    while True:
        clock.tick(FPS)        
        screen.fill(BGCOLOR)
        board.draw(screen)
        if board.gameover:
            text = FONT.render("RESTART", True, COLOR_INACTIVE if text_highlight else TEXT_COLOR)
        else: 
            text = FONT.render("AI MOVE", True, COLOR_INACTIVE if text_highlight else TEXT_COLOR)
        text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT + 40))
        screen.blit(text, text_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                button = event.button
                if text_rect.collidepoint(mouse_pos) and not board.gameover:
                    board.ai_move()
                elif text_rect.collidepoint(mouse_pos) and board.gameover:
                    return
                else:
                    board.handle_click(mouse_pos, button)

            elif event.type == pygame.MOUSEMOTION:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if text_rect.collidepoint(mouse_x, mouse_y):
                    text_highlight = True
                else: 
                    text_highlight = False


        if board.gameover:
            overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
            overlay.fill((0, 0, 0, 100)) 
            screen.blit(overlay, (0, 0))

            text = FONT.render("YOU WON!" if board.victory else "YOU LOST!", True, (255, 255, 255))
            text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
            screen.blit(text, text_rect)            

        pygame.display.update()