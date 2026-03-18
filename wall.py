import arcade
from arcade.color import BLUE_SAPPHIRE
from constants import *

class Wall(arcade.Sprite):
    def __init__(self, center_x, center_y):
        super().__init__()
        size = TILE_SIZE
        texture = arcade.make_soft_square_texture(size, BLUE_SAPPHIRE)
        self.texture = texture
        self.height = texture.height
        self.width = texture.width
        self.center_x = center_x
        self.center_y = center_y




