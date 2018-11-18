import pygame
import random
import grid
import textDisplay
from tweenColours import *

class overlay:
    def __init__(self, width, height):
        random.seed()
        self.startColour = self.pickNewColour()
        self.targetColour = self.pickNewColour()
        self.colour = self.startColour
        self.pos = (random.randrange(0,width), random.randrange(0,height))
        self.targetPos = (random.randrange(0,width), random.randrange(0,height))
        self.startPos = self.pos
        self.moveTime = 5
        self.startTime = 0
        self.width = width
        self.height = height

        self.grid = grid.Grid(self.width, self.height)
        self.history = textDisplay.textDisplay((10, 10), 230, 480)
        self.updatePosText()

        self.now = 0

    def draw(self, surface):
        self.grid.draw(surface, self.colour);

        pygame.draw.line(surface, self.colour, (0, self.pos[1]), (self.width, self.pos[1]))
        pygame.draw.line(surface, self.colour, (self.pos[0], 0), (self.pos[0], self.height))
        pygame.draw.circle(surface, self.colour, self.pos, 20, 1)
        pygame.draw.line(surface, self.colour, (self.pos[0] - 10, self.pos[1] - 10), (self.pos[0] - 18, self.pos[1] - 18))
        pygame.draw.line(surface, self.colour, (self.pos[0] + 10, self.pos[1] - 10), (self.pos[0] + 18, self.pos[1] - 18))
        pygame.draw.line(surface, self.colour, (self.pos[0] + 10, self.pos[1] + 10), (self.pos[0] + 18, self.pos[1] + 18))
        pygame.draw.line(surface, self.colour, (self.pos[0] - 10, self.pos[1] + 10), (self.pos[0] - 18, self.pos[1] + 18))
        
        self.history.draw(surface, self.colour)

    def updatePosText(self):
        self.history.updateCurrentText(''.join((str(self.pos[0]/10.0), ', ', str(self.pos[1]/10.0))), self.colour)

    def pickNewColour(self):
        red = random.randrange(10,255)
        green = random.randrange(10,255)
        blue = random.randrange(10,255)

        if red + green + blue < 255:
            selector = random.randrange(0,2)
            if selector == 0:
                red = random.randrange(200,255)
            if selector == 1:
                green = random.randrange(200,255)
            if selector == 2:
                blue = random.randrange(200,255)

        return (red, green, blue)

    def on_loop(self, updateTime):
        self.now += updateTime

        self.updatePosText()

        if self.pos == self.targetPos:
            self.target_reached()
        else:
            if self.now > self.startTime + self.moveTime:
                self.target_reached()
            else:
                timeOffset = (self.now - self.startTime) / self.moveTime
                xPos = self.startPos[0] + ((self.targetPos[0] - self.startPos[0]) * timeOffset)
                yPos = self.startPos[1] + ((self.targetPos[1] - self.startPos[1]) * timeOffset)
                self.colour = tweenColours(self.startColour, self.targetColour, timeOffset)
                self.pos = (int(round(xPos)), int(round(yPos)))

    def target_reached(self):
        self.now = 0
        self.pos = self.targetPos
        self.startPos = self.targetPos
        self.targetPos = (random.randrange(0, self.width), random.randrange(0, self.height))
        self.moveTime = random.randrange(2, 5)
        self.startColour = self.targetColour
        self.targetColour = self.pickNewColour()
        self.history.updateHistory()
