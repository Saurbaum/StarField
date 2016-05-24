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
        pass

    def draw(self, surface, colour):
        textSize = 24
        self.font.render_to(surface, self.pos, self.currentText, colour, None, 0, 0, textSize)
        index = 1
        for entry in self.history:
            self.font.render_to(surface, (self.pos[0], (self.pos[1] + index) * textSize), entry[0], entry[1], None, 0, 0, textSize)
            index = index + 1
        pass

    def updateCurrentText(self, text, colour):
        self.currentText = text
        self.currentColour = colour
        pass

    def updateHistory(self):
        self.history.append((self.currentText, self.currentColour))
        pass