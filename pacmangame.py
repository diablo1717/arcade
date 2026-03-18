import arcade
from wall import Wall
from coin import Coin 
from player import Player 
from enemy import Enemy 
from constants import *



class PacmanGame(arcade.View):
    def __init__(self):
        super().__init__()
        self.wall_list = arcade.SpriteList() 
        self.coin_list = arcade.SpriteList()
        self.ghost_list = arcade.SpriteList()
        self.player_list = arcade.SpriteList()
        self.player = None 
        self.game_over = False
        self.background_color = arcade.color.BLACK
        self.start_x = 0
        self.start_y = 0

    def setup(self):
        self.wall_list = arcade.SpriteList() 
        self.coin_list = arcade.SpriteList()
        self.ghost_list = arcade.SpriteList()
        self.player_list = arcade.SpriteList()
        self.game_over = False
        rows = len(LEVEL_MAP) 
        for row_idx, row in enumerate(LEVEL_MAP):
            for col_idx, cell in enumerate(row):
                x = col_idx * TILE_SIZE + TILE_SIZE / 2
                y = (rows - row_idx - 1) * TILE_SIZE + TILE_SIZE / 2
                if cell == "#":
                    self.wall_list.append(Wall(x, y))
                elif cell == ".":
                    self.coin_list.append(Coin(x, y))

                elif cell == "P":
                    print(f"x = {x}, y = {y}") 
                    self.player_list.append(Player(x, y, 0))

                elif cell == "G":
                    print(f"x = {x}, y = {y}") 
                    self.ghost_list.append(Enemy(x, y, 0))


    def on_draw(self):
        self.clear()
        self.wall_list.draw()
        self.coin_list.draw()
        self.ghost_list.draw() 
        self.player_list.draw()
        player = self.player_list[0]
        arcade.draw_text(f"score: {player.score}", 50, WINDOW_HEIGHT - 100)
        arcade.draw_text(f"lives: {player.lives}", 50, WINDOW_HEIGHT - 120)
        if self.game_over:
            arcade.draw_text(f"You lost!", WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2)
