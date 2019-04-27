""" A grid """

import math

import pygame

class Grid:
    """ A grid which will find a senssible number of squares for a given rectangle """
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.step = math.gcd(self.width, self.height) // 2
        self.horizontal_steps = self.width//self.step
        self.vertical_steps = self.height//self.step

        if self.horizontal_steps * self.vertical_steps < 30:
            self.step = self.step // 2
            self.horizontal_steps = self.width//self.step
            self.vertical_steps = self.height//self.step

    def draw(self, surface, colour):
        """ Renders the grid to the surface """
        pygame.draw.rect(surface, colour, (0, 0, self.width, self.height), 1)

        pos = self.step

        for _i in range(self.horizontal_steps):
            pygame.draw.line(surface, colour, (pos, 0), (pos, self.height))
            pos += self.step

        pos = self.step
        for _i in range(self.vertical_steps):
            pygame.draw.line(surface, colour, (0, pos), (self.width, pos))
            pos += self.step
