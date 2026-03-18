import arcade
from arcade.color import BLUEBONNET, REDWOOD, GREEN
from pacmangame import PacmanGame
from constants import *



def main():
    window = arcade.Window(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE)
    game = PacmanGame()
    game.setup()
    window.show_view(game)
    arcade.run()

main()