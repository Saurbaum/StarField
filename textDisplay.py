import pygame
import pygame.freetype as freetype
from collections import deque

class textDisplay:
    def __init__(self, pos, width, height):
        self.borderOverlap = 5
        self.pos = pos
        self.borderPos = (pos[0] - self.borderOverlap, pos[1] - self.borderOverlap)
        self.width = width
        self.borderWidth = width
        self.height = height
        self.borderHeight = height
        freetype.init()
        self.font = freetype.SysFont("Ariel", 24)
        self.currentText = ''
        self.currentColour = (0, 0, 0)
        self.history = deque()
        self.textSize = 24
        self.textSpace = 25

    def drawBorder(self, surface, colour):
        background = pygame.Surface((self.width, self.height), pygame.HWSURFACE)
        background.set_alpha(220)
        background.fill((colour[0]/5, colour[1]/5, colour[2]/5))

        pygame.draw.rect(background, colour, (0, 0, self.width, self.height), 1)

        surface.blit(background, self.borderPos)

    def draw(self, surface, colour):
        self.drawBorder(surface, colour)
        self.font.render_to(surface, self.pos, self.currentText, colour, None, 0, 0, self.textSize)
        index = len(self.history)
        for entry in self.history:
            self.font.render_to(surface, (self.pos[0], self.pos[1] + (index * self.textSpace)), entry[0], entry[1], None, 0, 0, self.textSize)
            index = index - 1

    def updateCurrentText(self, text, colour):
        self.currentText = text
        self.currentColour = colour

    def updateHistory(self):
        self.history.append((self.currentText, self.currentColour))
        if (len(self.history) + 1) * self.textSpace > self.height:
            self.history.popleft()