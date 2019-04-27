""" Starfield scanner """

import pygame
import overlay
import stars

class StarfieldScanner:
    """Provides a grid and scanning reticle over a field of randomly generated stars"""
    def __init__(self, width, height, displaySurface):
        self.rendering = True
        self._display_surf = displaySurface
        self.overlay = overlay.Overlay(width, height)
        self.stars = stars.Stars(width, height)
        self.now = 0
        self.regenerate_stars_trigger = 1

    def draw_overlay(self):
        """ Draws the overlay """
        self.overlay.draw(self._display_surf)

    def draw_starfield(self):
        """ Draws the starfield """
        self.stars.draw(self._display_surf)

    def on_loop(self, update_time):
        """ Update loop """
        self.now += update_time
        if self.now >= self.regenerate_stars_trigger:
            self.stars.update_starfield()
            self.now -= self.regenerate_stars_trigger

        self.overlay.on_loop(update_time)

    def on_render(self):
        """ Render event """
        self._display_surf.fill((0, 0, 0))
        self.draw_starfield()
        self.draw_overlay()
        pygame.display.update()

    def key_press(self, key):
        """ user input test """
        if key == pygame.K_SPACE:
            self.stars.update_starfield()
