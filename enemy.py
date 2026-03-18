from character import *
import random
from arcade.color import RED 

class Enemy(arcade.Sprite):
    def __init__(self, center_x, center_y, speed):
        super().__init__()
        radius = TILE_SIZE
        texture = arcade.make_circle_texture(radius * 2, RED)
        self.texture = texture
        self.width = texture.width - 9
        self.height = texture.height - 9
        self.center_x = center_x
        self.center_y = center_y
        self.time_to_change_direction = 0

    def pick_new_direction(self):
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (0, 0)]
        direction = random.choice(directions)
        self.change_x = direction[0]
        self.change_y = direction[1]
        self.time_to_change_direction = random.uniform(0.3, 1.0)

    def update(self ,delta_time=1/60):
        self.time_to_change_direction -= delta_time
        if self.time_to_change_direction <= 0:
            self.pick_new_direction()
            self.center_x = self.change_x * self.speed
            self.center_y = self.change_y * self.speed






