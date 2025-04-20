from game import game_loop
from menu import menu_loop
from gamestate import GameState

if __name__ == "__main__":
    while True:
        state = GameState()
        menu_loop(state)
        game_loop(state.rows, state.cols, state.mines)
