""" Overlay """

import random
import pygame
import grid
import text_display
from tween_colours import tween_colours

class Overlay:
    """ An overlay is a grid and targeting reticle that will track around the screen """
    def __init__(self, width, height):
        random.seed()
        self.start_colour = self.pick_new_colour()
        self.target_colour = self.pick_new_colour()
        self.colour = self.start_colour
        self.pos = (random.randrange(0, width), random.randrange(0, height))
        self.target_pos = (random.randrange(0, width), random.randrange(0, height))
        self.start_pos = self.pos
        self.move_time = 5
        self.start_time = 0
        self.width = width
        self.height = height

        self.grid = grid.Grid(self.width, self.height)
        self.history = text_display.TextDisplay((10, 10), 230, 480)
        self.update_pos_text()

        self.now = 0

    def draw(self, surface):
        """ Draw the overlay """
        self.grid.draw(surface, self.colour)

        pygame.draw.line(surface, self.colour, (0, self.pos[1]), (self.width, self.pos[1]))
        pygame.draw.line(surface, self.colour, (self.pos[0], 0), (self.pos[0], self.height))
        pygame.draw.circle(surface, self.colour, self.pos, 20, 1)
        pygame.draw.line(surface, self.colour, (self.pos[0] - 10, self.pos[1] - 10), (self.pos[0] - 18, self.pos[1] - 18))
        pygame.draw.line(surface, self.colour, (self.pos[0] + 10, self.pos[1] - 10), (self.pos[0] + 18, self.pos[1] - 18))
        pygame.draw.line(surface, self.colour, (self.pos[0] + 10, self.pos[1] + 10), (self.pos[0] + 18, self.pos[1] + 18))
        pygame.draw.line(surface, self.colour, (self.pos[0] - 10, self.pos[1] + 10), (self.pos[0] - 18, self.pos[1] + 18))

        self.history.draw(surface, self.colour)

    def update_pos_text(self):
        """ Update the current position on the history """
        self.history.update_current_text(''.join((str(self.pos[0]/10.0), ', ', str(self.pos[1]/10.0))), self.colour)

    def pick_new_colour(self):
        """ Generates a new random colour """
        red = random.randrange(10, 255)
        green = random.randrange(10, 255)
        blue = random.randrange(10, 255)
        alpha = random.randrange(128, 255)

        if red + green + blue < 255:
            selector = random.randrange(0, 2)
            if selector == 0:
                red = random.randrange(200, 255)
            if selector == 1:
                green = random.randrange(200, 255)
            if selector == 2:
                blue = random.randrange(200, 255)

        return (red, green, blue, alpha)

    def on_loop(self, update_time):
        """ Update loop """
        self.now += update_time

        self.update_pos_text()

        if self.pos == self.target_pos:
            self.target_reached()
        else:
            if self.now > self.start_time + self.move_time:
                self.target_reached()
            else:
                time_offset = (self.now - self.start_time) / self.move_time
                x_pos = self.start_pos[0] + ((self.target_pos[0] - self.start_pos[0]) * time_offset)
                y_pos = self.start_pos[1] + ((self.target_pos[1] - self.start_pos[1]) * time_offset)
                self.colour = tween_colours(self.start_colour, self.target_colour, time_offset)
                self.pos = (int(round(x_pos)), int(round(y_pos)))

    def target_reached(self):
        """ Set a new target for the overlay """
        self.now = 0
        self.pos = self.target_pos
        self.start_pos = self.target_pos
        self.target_pos = (random.randrange(0, self.width), random.randrange(0, self.height))
        self.move_time = random.randrange(2, 5)
        self.start_colour = self.target_colour
        self.target_colour = self.pick_new_colour()
        self.history.update_history()
