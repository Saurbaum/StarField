""" Gauge panel """

import pygame
import random
from enum import Enum

class Gague_Direction(Enum):
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4

class Gauge:
    """A gauges"""
    def __init__(self, x_pos, y_pos, width, height, max_value, direction: Gague_Direction, displaySurface):
        self.rendering = True
        self._display_surf = displaySurface
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.width = width
        self.height = height

        self.bar_width = self.width - (self.width / 10)
        self.bar_max_height = self.height - 10
        self.bar_x_pos = (self.width - self.bar_width) / 2
        self.bar_y_pos = (self.height - self.bar_max_height) / 2

        self.max_value = max_value
        self.current_value = 0
        self.start_value = 0
        self.target_value = self.current_value

        self.move_time = 1.0
        self.start_time = 0

        self.bar_direction = direction

        self.now = 0
        
    def on_loop(self, update_time):
        """ Update loop """
        self.now += update_time
        time_offset = (self.now - self.start_time) / self.move_time

        if self.current_value == self.target_value:
            self.target_reached()
        else:
            if self.now > self.move_time:
                self.target_reached()
            else:
                self.current_value = self.current_value + ((self.target_value - self.start_value) * time_offset)

    def target_reached(self):
        self.now = 0
        self.current_value = self.target_value
        self.target_value = random.randrange(0, self.max_value)

    def on_render(self):
        """ Render event """
        background = pygame.Surface((self.width, self.height), pygame.HWSURFACE)
        background.fill((128, 128, 128))

        height = self.bar_max_height * (self.current_value / self.max_value)

        bar = pygame.Surface((self.bar_width, height), pygame.HWSURFACE)
        bar.fill((20, 20, 20))
        background.blit(bar, (self.bar_x_pos, self.bar_y_pos))

        match self.bar_direction:
            case Gague_Direction.UP:
                background = pygame.transform.rotate(background, 180)
            case Gague_Direction.DOWN:
                background = pygame.transform.rotate(background, 0)
            case Gague_Direction.LEFT:
                background = pygame.transform.rotate(background, 270)
            case Gague_Direction.RIGHT:
                background = pygame.transform.rotate(background, 90)

        self._display_surf.blit(background, (self.x_pos, self.y_pos))
        
    def key_press(self, key):
        """ user input test """
        #if key == pygame.K_SPACE:

    def set_current_value(self, value):
        self.now = 0
        self.start_value = self.current_value
        self.target_value = value
