from character import Character

class Player(Character):
    def __init__(self, center_x, center_y, speed):
        super().__init__(center_x, center_y, speed)
        self.score = 0
        self.lives = 3


    def move(self):
        self.center_x += self.change_x * self.speed
        self.center_y += self.change_y * self.speed


