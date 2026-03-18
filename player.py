from arcade.color import YELLOW
from constants import *
from character import Character
import arcade

class Player(arcade.Sprite):
    def __init__(self, center_x, center_y, speed):
        super().__init__()
        radius = TILE_SIZE
        texture = arcade.make_circle_texture(radius * 2, YELLOW)
        self.texture = texture
        self.width = texture.width - 9
        self.height = texture.height - 9
        self.center_x = center_x 
        self.center_y = center_y
        self.speed = speed
        self.score = 0
        self.lives = 3


    def move(self):
        self.center_x += self.change_x * self.speed
        self.center_y += self.change_y * self.speed


