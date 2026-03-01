from character import Character
import random

class Enemy(Character):
    def __init__(self, center_x, center_y, speed):
        super().__init__(center_x, center_y, speed)
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






