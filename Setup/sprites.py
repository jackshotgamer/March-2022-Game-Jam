import pathlib
import arcade
from functools import cache

SPRITE_PATH = pathlib.Path('./Sprites/')


@cache
def load_sprite(filename):
    return arcade.load_texture(SPRITE_PATH/f'{filename}.png')



