""" Gauge panel """

import pygame

class Gauge:
    """A gauges"""
    def __init__(self, x_pos, y_pos, width, height, displaySurface):
        self.rendering = True
        self._display_surf = displaySurface
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.width = width
        self.height = height
        self.now = 0
        
    def on_loop(self, update_time):
        """ Update loop """
        self.now += update_time

    def on_render(self):
        """ Render event """
        background = pygame.Surface((self.width, self.height), pygame.HWSURFACE)
        background.fill((128, 128, 128))
        self._display_surf.blit(background, (self.x_pos, self.y_pos))

    def key_press(self, key):
        """ user input test """
        #if key == pygame.K_SPACE:
            