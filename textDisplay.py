import pygame
import pygame.freetype as freetype
from collections import deque

class textDisplay:
    def __init__(self, pos, width, height):
        self.pos = pos
        self.width = width
        self.height = height
        freetype.init()
        self.font = freetype.SysFont("Ariel", 24)
        self.currentText = ''
        self.currentColour = (0, 0, 0)
        self.history = deque()
        self.textSize = 24
        pass

    def draw(self, surface, colour):
        pygame.draw.line(surface, colour, (self.pos[0], self.pos[1]), (self.pos[0] + self.width, self.pos[1]))
        pygame.draw.line(surface, colour, (self.pos[0] + self.width, self.pos[1]), (self.pos[0] + self.width, self.pos[1] + self.height))
        pygame.draw.line(surface, colour, (self.pos[0] + self.width, self.pos[1] + self.height), (self.pos[0], self.pos[1] + self.height))
        pygame.draw.line(surface, colour, (self.pos[0], self.pos[1] + self.height), (self.pos[0], self.pos[1]))
        self.font.render_to(surface, self.pos, self.currentText, colour, None, 0, 0, self.textSize)
        index = len(self.history)
        for entry in self.history:
            self.font.render_to(surface, (self.pos[0], self.pos[1] + (index * self.textSize)), entry[0], entry[1], None, 0, 0, self.textSize)
            index = index - 1
        pass

    def updateCurrentText(self, text, colour):
        self.currentText = text
        self.currentColour = colour
        pass

    def updateHistory(self):
        self.history.append((self.currentText, self.currentColour))
        if (len(self.history)) * self.textSize > self.height:
            self.history.popleft()
        pass