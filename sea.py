""" Sea display """

import pygame
import ship

class Sea:
    """A Sea play area"""
    def __init__(self, width, height, displaySurface):
        self.rendering = True
        self._display_surf = displaySurface
        self.now = 0
        self.width = width
        self.height = height

        self.player_ship =  ship.Ship(200, 200, self._display_surf)

    def on_loop(self, update_time):
        """ Update loop """
        self.now += update_time
        self.player_ship.on_loop(update_time)

    def on_render(self):
        """ Render event """
        background_color = (56, 56, 255)
        self._display_surf.fill(background_color)

        self.player_ship.on_render(background_color)

        pygame.display.update()

    def key_press(self, key):
        """ user input test """
        self.player_ship.key_press(key)
            