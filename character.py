import arcade
from constants import * 

class Character(arcade.Sprite):
    def __init__(self, speed, x, y, color):
        super().__init__()
        radius = TILE_SIZE
        texture = arcade.make_circle_texture(radius * 2, color)
        self.texture = texture
        self.width = texture.width - 9
        self.height = texture.height - 9
        self.center_x = x
        self.center_y = y
        self.speed = speed




