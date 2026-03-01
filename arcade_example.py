import arcade
from arcade.color import BLUEBONNET, REDWOOD, GREEN


def main():
    window = arcade.Window(800, 600)
    arcade.draw_circle_filled(400, 300, 30, BLUEBONNET)
    arcade.draw_ellipse_filled(600, 300, 50, 20, REDWOOD)
    arcade.draw_text("Ori Golan", 500, 400, GREEN)

    wall_list = arcade.SpriteList()

    arcade.run()

main()