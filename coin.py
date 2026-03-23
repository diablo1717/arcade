import arcade
from arcade.color import YELLOW
from constants import *

class Coin(arcade.Sprite):
    def __init__(self, center_x, center_y, value=10):
        super().__init__()
        radius = TILE_SIZE // 2
        texture = arcade.make_circle_texture(radius, YELLOW)
        self.texture = texture
        self.width = texture.width - 4
        self.height = texture.height - 4
        self.center_x = center_x
        self.center_y = center_y
        self.value = value
