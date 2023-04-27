"""Blips for displaying on a radar"""

import pygame
from tween_colours import tween_colours

class Blip:
    """A blip to draw on a display"""
    def __init__(self, pos, startTime, strength, fade_time, colour, fade_colour):
        self.pos = pos
        self.fade_time = fade_time
        self.start_time = startTime
        self.update_time = startTime
        self.strength = strength
        self.progress = 0
        self.colour = colour
        self.fade_colour = fade_colour

    def on_render(self, surface):
        if self.start_time == -1:
            return

        if self.progress >= 1.0 or self.progress < 0:
            self.start_time = -1
            return

        steps = int(self.strength * (1 - self.progress))

        for size in range(steps):
            value = self.strength - size
            time_offset = (value) / self.strength
            pygame.draw.circle(surface, tween_colours(self.colour, self.fade_colour, time_offset), self.pos, value)

    def on_loop(self, update_time):
        self.update_time += update_time

        if self.start_time == -1:
            return

        self.progress = (self.update_time - self.start_time) / self.fade_time

        if self.progress >= 1.0 or self.progress < 0:
            self.start_time = -1
