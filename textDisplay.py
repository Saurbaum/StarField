import pygame
import pygame.freetype as freetype
from collections import deque

class textDisplay:
    def __init__(self, pos, width, height):
        self.pos = pos
        self.borderPos = (pos[0] - 5, pos[1] - 5)
        self.width = width
        self.borderWidth = width + 5
        self.height = height
        self.borderHeight = height + 5
        freetype.init()
        self.font = freetype.SysFont("Ariel", 24)
        self.currentText = ''
        self.currentColour = (0, 0, 0)
        self.history = deque()
        self.textSize = 24
        pass

    def drawBorder(self, surface, colour):
        pygame.draw.line(surface, (colour[0]/5, colour[1]/5, colour[2]/5), (self.borderPos[0], self.borderPos[1] + (self.borderHeight/2)), (self.borderPos[0] + self.borderWidth, self.borderPos[1] + (self.borderHeight/2)), self.borderHeight)

        pygame.draw.line(surface, colour, (self.borderPos[0], self.borderPos[1]), (self.borderPos[0] + self.borderWidth, self.borderPos[1]), 2)
        pygame.draw.line(surface, colour, (self.borderPos[0] + self.borderWidth, self.borderPos[1]), (self.borderPos[0] + self.borderWidth, self.borderPos[1] + self.borderHeight), 2)
        pygame.draw.line(surface, colour, (self.borderPos[0] + self.borderWidth, self.borderPos[1] + self.borderHeight), (self.borderPos[0], self.borderPos[1] + self.borderHeight), 2)
        pygame.draw.line(surface, colour, (self.borderPos[0], self.borderPos[1] + self.borderHeight), (self.borderPos[0], self.borderPos[1]), 2)
        pass

    def draw(self, surface, colour):
        self.drawBorder(surface, colour)
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