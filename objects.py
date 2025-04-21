import pygame
from settings import *
import random
import time

# "?" unknown
# "x" mine
# "1-8" clue
# "0" empty

class Tile:
    def __init__(self, x, y, image, type, tilesize, revealed=False, flagged=False, ):
        self.tilenumbers = []

        for i in range(1, 9):
            self.tilenumbers.append(pygame.transform.scale(pygame.image.load(os.path.join(dirname, f"Assets\Tile{i}.png")), (tilesize, tilesize)))

        self.tileempty = pygame.transform.scale(pygame.image.load(os.path.join(dirname, "Assets\TileEmpty.png")), (tilesize, tilesize))
        self.tileexploded = pygame.transform.scale(pygame.image.load(os.path.join(dirname, "Assets\TileExploded.png")), (tilesize, tilesize))
        self.tileflag = pygame.transform.scale(pygame.image.load(os.path.join(dirname, "Assets\TileFlag.png")), (tilesize, tilesize))
        self.tilemine = pygame.transform.scale(pygame.image.load(os.path.join(dirname, "Assets\TileMine.png")), (tilesize, tilesize))
        self.tilenotmine = pygame.transform.scale(pygame.image.load(os.path.join(dirname, "Assets\TileNotMine.png")), (tilesize, tilesize))
        self.tileunknown = pygame.transform.scale(pygame.image.load(os.path.join(dirname, "Assets\TileUnknown.png")), (tilesize, tilesize))

        self.x, self.y = tilesize * x, tilesize * y
        self.image = image
        self.type = type
        self.revealed = revealed
        self.flagged = flagged
        self.clicked_ai = False

    def draw(self, board_surface):
        if self.flagged:
            board_surface.blit(self.tileflag, (self.x, self.y))
        elif self.revealed:
            if self.type == "x":
                board_surface.blit(self.tileexploded, (self.x, self.y))
            else:
                board_surface.blit(self.image, (self.x, self.y))
        else:
            board_surface.blit(self.tileunknown, (self.x, self.y))

    def __repr__(self):
        return self.type if self.revealed else "?"

class Board:
    def __init__(self, tilesize, rows, cols, mines):
        self.tilenumbers = []
        self.mines = mines
        self.rows = rows
        self.cols = cols
        self.gameover = False
        self.victory = False
        self.first_click = True
        self.no_moves = False

        for i in range(1, 9):
            self.tilenumbers.append(pygame.transform.scale(pygame.image.load(os.path.join(dirname, f"Assets\Tile{i}.png")), (tilesize, tilesize)))

        self.tileempty = pygame.transform.scale(pygame.image.load(os.path.join(dirname, "Assets\TileEmpty.png")), (tilesize, tilesize))
        self.tileexploded = pygame.transform.scale(pygame.image.load(os.path.join(dirname, "Assets\TileExploded.png")), (tilesize, tilesize))
        self.tileflag = pygame.transform.scale(pygame.image.load(os.path.join(dirname, "Assets\TileFlag.png")), (tilesize, tilesize))
        self.tilemine = pygame.transform.scale(pygame.image.load(os.path.join(dirname, "Assets\TileMine.png")), (tilesize, tilesize))
        self.tilenotmine = pygame.transform.scale(pygame.image.load(os.path.join(dirname, "Assets\TileNotMine.png")), (tilesize, tilesize))
        self.tileunknown = pygame.transform.scale(pygame.image.load(os.path.join(dirname, "Assets\TileUnknown.png")), (tilesize, tilesize))

        self.tilesize = tilesize
        self.board_surface = pygame.Surface((WIDTH, HEIGHT))
        self.board_list = [[Tile(col, row, self.tileempty, "?", self.tilesize) for row in range(self.rows)] for col in range(self.cols)]
        self.dug = []

    def ai_move(self):
        self.check_clues()
        self.click_around()


    def check_clues(self):
        self.no_moves = True
        for row in self.board_list:
            for tile in row:
                x = tile.x // self.tilesize
                y = tile.y // self.tilesize
                unknown = []
                if tile.revealed and tile.type in (str(i) for i in range(1, 9)):
                    for x_offset in range(-1, 2):
                        for y_offset in range(-1, 2):
                            if x + x_offset >= 0 and x + x_offset < self.rows and y + y_offset >= 0 and y + y_offset < self.cols:
                                if not self.board_list[x + x_offset][y + y_offset].revealed:
                                    unknown.append(self.board_list[x + x_offset][y + y_offset])

                    if len(unknown) == int(tile.type):
                        for tile in unknown:
                            if not tile.flagged and not tile.clicked_ai:
                                tile.clicked_ai = True
                                tile.flagged = True
                                self.no_moves = False
        
    def click_around(self):
        for row in self.board_list:
            for tile in row:
                if tile.type in (str(i) for i in range(1, 9)) and tile.revealed:
                    x = tile.x // self.tilesize
                    y = tile.y // self.tilesize
                    clicked = []
                    for x_offset in range(-1, 2):
                        for y_offset in range(-1, 2):
                            if x + x_offset >= 0 and x + x_offset < self.rows and y + y_offset >= 0 and y + y_offset < self.cols:
                                if self.board_list[x + x_offset][y + y_offset].clicked_ai:
                                    clicked.append(self.board_list[x + x_offset][y + y_offset])

                    if len(clicked) == int(tile.type):
                        for x_offset in range(-1, 2):
                            for y_offset in range(-1, 2):
                                if x + x_offset >= 0 and x + x_offset < self.rows and y + y_offset >= 0 and y + y_offset < self.cols:
                                    self.dig(x + x_offset, y + y_offset)
                                    self.check_victory()


    def handle_click(self, mouse_pos, button):
        x, y = mouse_pos
        x //= self.tilesize
        y //= self.tilesize

        self.no_moves = False
        if button == 1:
            if not self.board_list[x][y].flagged and (x, y) not in self.dug:
                self.dig(x, y)
                self.display()
                self.check_victory()
        elif button == 3:
            if (x, y) not in self.dug:
                self.board_list[x][y].flagged = not self.board_list[x][y].flagged

    def game_over(self):
        for row in self.board_list:
            for tile in row:
                tile.revealed = True
                if tile.type == "x" and tile.flagged:
                    tile.flagged = False
                    tile.image = self.tilemine

                elif tile.type != "x" and tile.flagged:
                    tile.flagged = False
                    tile.image = self.tilenotmine
        self.gameover = True

    def dig(self, x, y):
        if self.first_click:
            self.first_click = False
            self.place_mines(x, y)
            self.place_clues()

        if not self.board_list[x][y].flagged:
            self.dug.append((x, y))
            if self.board_list[x][y].type == "x":
                self.board_list[x][y].revealed = True
                self.game_over()
                return False
            elif self.board_list[x][y].type in (str(i) for i in range(1, 9)):
                self.board_list[x][y].revealed = True
                return True
            
            self.board_list[x][y].revealed = True
            for x_offset in range(-1, 2):
                for y_offset in range(-1, 2):
                    if x + x_offset >= 0 and x + x_offset < self.rows and y + y_offset >= 0 and y + y_offset < self.cols:
                        if (x + x_offset, y + y_offset) not in self.dug:
                            self.dig(x + x_offset, y + y_offset)
        

    def place_mines(self, x, y):
        excluded_tiles = []
        placed_mines = 0
        for x_offset in range(-1, 2):
            for y_offset in range(-1, 2):
                if x + x_offset >= 0 and x + x_offset < self.rows and y + y_offset >= 0 and y + y_offset < self.cols:
                    excluded_tiles.append((x + x_offset, y + y_offset))
                    
        for tile in range(self.mines):
            if placed_mines >= self.rows * self.cols - len(excluded_tiles):
                self.mines = placed_mines
                self.check_victory()
                break

            while True:
                x_pos = random.randint(0, self.rows-1)
                y_pos = random.randint(0, self.cols-1)

                if self.board_list[x_pos][y_pos].type == "?" and (x_pos, y_pos) not in excluded_tiles:
                    self.board_list[x_pos][y_pos].image = self.tilemine
                    self.board_list[x_pos][y_pos].type = "x"
                    placed_mines += 1
                    break

    def check_victory(self):
        unknown_count = 0
        for row in self.board_list:
            for tile in row:
                if not tile.revealed:
                    unknown_count += 1
        if unknown_count == self.mines:
            for row in self.board_list:
                for tile in row:
                    if not tile.revealed:
                        tile.flagged = True

            self.victory = True
            self.gameover = True

    def place_clues(self):
        for row in range(self.rows):
            for col in range(self.cols):
                if self.board_list[row][col].type != "x":
                    num_mines = self.check_neighbors(row, col)
                    if num_mines > 0:
                        self.board_list[row][col].image = self.tilenumbers[num_mines-1]
                        self.board_list[row][col].type = str(num_mines)
                    else:
                        self.board_list[row][col].image = self.tileempty
                        self.board_list[row][col].type = "0"
                    

    def check_neighbors(self, x, y):
        num_mines = 0 
        for x_offset in range(-1, 2):
            for y_offset in range(-1, 2):
                if x + x_offset >= 0 and x + x_offset < self.rows and y + y_offset >= 0 and y + y_offset < self.cols:
                    if self.board_list[x + x_offset][y + y_offset].type == "x":
                        num_mines += 1
        return num_mines

    def draw(self, screen):
        for row in self.board_list:
            for tile in row:
                tile.draw(self.board_surface)
        screen.blit(self.board_surface, (0, 0))



    def display(self):
        for row in self.board_list:
            print(row)
        print("\n")