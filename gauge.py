""" Gauge panel """

import pygame

class Gauge:
    """A gauges"""
    def __init__(self, x_pos, y_pos, width, height, max_value, displaySurface):
        self.rendering = True
        self._display_surf = displaySurface
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.width = width
        self.height = height

        self.bar_width = self.width - (self.width / 10)
        self.bar_max_height = self.height - (self.height / 10)

        self.max_value = max_value
        self.current_value = 0
        self.target_value = self.current_value

        self.move_time = 1.0

        self.now = 0
        
    def on_loop(self, update_time):
        """ Update loop """
        self.now += update_time

        if self.current_value != self.target_value:
            self.target_reached()
        else:
            if self.now > self.start_time + self.move_time:
                self.target_reached()
            else:
                time_offset = (self.now - self.start_time) / self.move_time
                self.current_value = self.self.current_value + ((self.target_value - self.start_value) * time_offset)

    def target_reached(self):
        self.now = 0
        self.current_value = self.target_value

    def on_render(self):
        """ Render event """
        background = pygame.Surface((self.width, self.height), pygame.HWSURFACE)
        background.fill((128, 128, 128))

        height = self.bar_height * ()

        bar = pygame.Surface((self.bar_width, height), pygame.HWSURFACE)

        self._display_surf.blit(background, (self.x_pos, self.y_pos))

    def key_press(self, key):
        """ user input test """
        #if key == pygame.K_SPACE:

    def set_current_value(self, value):
        self.now = 0
        self.start_value = self.current_value
        self.target_value = value
