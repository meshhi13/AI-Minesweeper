import pygame
import sys
from settings import *
from game import *
from gamestate import *


def menu_loop(state):
    menu_items = ["PLAY", f"SIZE: {state.rows}", f"MINES: {state.mines}", "QUIT"]
    selected_index = 0
    
    while True:
        screen.fill(BGCOLOR)
        
        for i, item in enumerate(menu_items):
            if i == selected_index:
                color = COLOR_INACTIVE
            else:
                color = TEXT_COLOR
            text = FONT.render(item, True, color)
            rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + (i-1.5) * 70))
            screen.blit(text, rect)
            pygame.display.flip()
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.MOUSEMOTION:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                for i, item in enumerate(menu_items):
                    text = FONT.render(item, True, WHITE)
                    rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + (i-1.5) * 70))
                    if rect.collidepoint(mouse_x, mouse_y):
                        selected_index = i

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if menu_items[selected_index] == "PLAY":
                        return
                    elif menu_items[selected_index].startswith("SIZE:"):
                        state.rows = next(SIZES)
                        menu_items[1] = f"SIZE: {state.rows}"
                        state.cols = state.rows
                    elif menu_items[selected_index].startswith("MINES:"):
                        state.mines = next(MINES)
                        menu_items[2] = f"MINES: {state.mines}"
                    elif menu_items[selected_index] == "QUIT":
                        pygame.quit()
                        sys.exit()

        clock.tick(30)
