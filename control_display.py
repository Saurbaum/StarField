""" Control display """

import pygame

class ControlDisplay:
    """A panel of gauges"""
    def __init__(self, width, height, displaySurface):
        self.rendering = True
        self._display_surf = displaySurface
        self.now = 0
        
    def on_loop(self, update_time):
        """ Update loop """
        self.now += update_time

    def on_render(self):
        """ Render event """
        self._display_surf.fill((255, 0, 255))
        
        pygame.display.update()

    def key_press(self, key):
        """ user input test """
        #if key == pygame.K_SPACE:
            