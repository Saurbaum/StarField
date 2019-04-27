""" Text Display """

from collections import deque
import pygame
import pygame.freetype as freetype

class TextDisplay:
    """ A display of a box background and text on screen """
    def __init__(self, pos, width, height):
        self.border_overlap = 5
        self.pos = pos
        self.border_pos = (pos[0] - self.border_overlap, pos[1] - self.border_overlap)
        self.width = width
        self.border_width = width
        self.height = height
        self.border_height = height
        freetype.init()
        self.font = freetype.SysFont("Ariel", 24)
        self.current_text = ''
        self.current_colour = (0, 0, 0)
        self.history = deque()
        self.text_size = 24
        self.text_space = 25

    def draw_border(self, surface, colour):
        """ Draw a border around the area in a slightly brighter colour """
        background = pygame.Surface((self.width, self.height), pygame.HWSURFACE)
        background.set_alpha(220)
        background.fill((colour[0]/5, colour[1]/5, colour[2]/5))

        pygame.draw.rect(background, colour, (0, 0, self.width, self.height), 1)

        surface.blit(background, self.border_pos)

    def draw(self, surface, colour):
        """ Rander the text display """
        self.draw_border(surface, colour)
        self.font.render_to(surface, self.pos, self.current_text, colour, None, 0, 0, self.text_size)
        index = len(self.history)
        for entry in self.history:
            self.font.render_to(surface, \
                (self.pos[0], self.pos[1] + (index * self.text_space)), entry[0], entry[1], None, 0, 0, self.text_size)
            index = index - 1

    def update_current_text(self, text, colour):
        """ Update the text at the top of the display """
        self.current_text = text
        self.current_colour = colour

    def update_history(self):
        """ A a new entry into the history """
        self.history.append((self.current_text, self.current_colour))
        if (len(self.history) + 1) * self.text_space > self.height:
            self.history.popleft()
