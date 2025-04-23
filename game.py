import pygame
from settings import *
from objects import *
import sys

def game_loop(rows, cols, mines):
    tilesize = WIDTH // cols
    board = Board(tilesize, rows, cols, mines)
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
            mouse_x, mouse_y = pygame.mouse.get_pos()
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
                elif mouse_x > 0 and mouse_x < WIDTH and mouse_y > 0 and mouse_y < HEIGHT:
                    board.handle_click(mouse_pos, button)

            elif event.type == pygame.MOUSEMOTION:
                if text_rect.collidepoint(mouse_x, mouse_y):
                    text_highlight = True
                else: 
                    text_highlight = False


        if board.gameover:
            overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
            overlay.fill((0, 0, 0, 100)) 
            screen.blit(overlay, (0, 0))

            text = FONT.render("YOU WON!" if board.victory else "YOU LOST!", True, TEXT_COLOR)
            text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
            screen.blit(text, text_rect)   

        if board.no_moves:
            text1 = FONT.render("NO MOVES FOUND", True, TEXT_COLOR)
            text1_rect = text1.get_rect(center=(WIDTH // 2, HEIGHT // 2 - text1.get_height() // 2 - 10))
            text2 = FONT.render("CLICK A TILE", True, TEXT_COLOR)
            text2_rect = text2.get_rect(center=(WIDTH // 2, HEIGHT // 2 + text2.get_height() // 2 + 10))

            text_bg = pygame.Surface((2 * WIDTH // 3, text1.get_height() * 3), pygame.SRCALPHA)
            text_bg.fill((0, 0, 0, 150)) 
            text_bg_rect = text_bg.get_rect(center=(WIDTH // 2, HEIGHT // 2))
            screen.blit(text_bg, text_bg_rect)
            screen.blit(text2, text2_rect)
            screen.blit(text1, text1_rect)


        pygame.display.update()
