"""Target for moving around"""

import random
import pygame
class Target:
    """A Target to move around the screen"""
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.now = 0
        self.start_time = 0
        self.move_time = random.randrange(50, 75)
        self.pos = (random.randrange(0, width), random.randrange(0, height))
        self.start_pos = self.pos
        self.target_pos = (random.randrange(0, width), random.randrange(0, height))

        self.strength = 50

    def on_render(self, surface, translate):
        ''' Translate is a multiplier that needs to shift a point based on how much of the screen is in view '''
        pygame.draw.circle(surface, (128,128,128), (self.pos[0], self.pos[1]), 5)

    def on_loop(self, update_time):
        """Main update loop"""
        self.now += update_time

        if self.pos == self.target_pos:
            self.target_reached()
        else:
            if self.now > self.start_time + self.move_time:
                self.target_reached()
            else:
                time_offset = (self.now - self.start_time) / self.move_time
                x_pos = self.start_pos[0] + ((self.target_pos[0] - self.start_pos[0]) * time_offset)
                y_pos = self.start_pos[1] + ((self.target_pos[1] - self.start_pos[1]) * time_offset)
                self.pos = (int(round(x_pos)), int(round(y_pos)))

    def target_reached(self):
        """Blip has reached the target positions"""
        self.now = 0
        self.pos = self.target_pos
        self.start_pos = self.target_pos
        self.target_pos = (random.randrange(0, self.width), random.randrange(0, self.height))
        self.move_time = random.randrange(50, 75)
