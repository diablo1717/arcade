import arcade
from arcade.color import BLUEBONNET, REDWOOD, GREEN
from pacmangame import PacmanGame
from constants import *


#NOTE: for some reason the game treats the Ghost and the player as the same
# couldn't fix it, sorry

def main():
    window = arcade.Window(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE)
    game = PacmanGame()
    game.setup()
    window.show_view(game)
    arcade.run()

main()