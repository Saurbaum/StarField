import pygame
import pygame.freetype as freetype

class textDisplay:
    def __init__(self, pos, width, height):
        self.pos = pos
        self.width = width
        self.height = height
        freetype.init()
        self.font = freetype.SysFont("Ariel", 24)
        currentText = ''
        pass

    def draw(self, surface, colour):
        textSize = 24
        self.font.render_to(surface, self.pos, self.currentText, colour, None, 0, 0, textSize)
        pass

    def updateCurrentText(self, text):
        self.currentText = text
        pass

    def updateHistory(self):
        pass