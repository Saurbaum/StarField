import pygame
import pygame.freetype as freetype
import random

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
        self.startTime = 0;
        self.width = width
        self.height = height
        self.updatePosText()
        freetype.init()
        self.font = freetype.SysFont("Ariel", 72)

    def draw(self, surface):
        pygame.draw.line(surface, self.colour, (0, self.pos[1]), (self.width, self.pos[1]))
        pygame.draw.line(surface, self.colour, (self.pos[0], 0), (self.pos[0], self.height))
        pygame.draw.circle(surface, self.colour, self.pos, 20, 1)
        pygame.draw.line(surface, self.colour, (self.pos[0] - 10, self.pos[1] - 10), (self.pos[0] - 18, self.pos[1] - 18))
        pygame.draw.line(surface, self.colour, (self.pos[0] + 10, self.pos[1] - 10), (self.pos[0] + 18, self.pos[1] - 18))
        pygame.draw.line(surface, self.colour, (self.pos[0] + 10, self.pos[1] + 10), (self.pos[0] + 18, self.pos[1] + 18))
        pygame.draw.line(surface, self.colour, (self.pos[0] - 10, self.pos[1] + 10), (self.pos[0] - 18, self.pos[1] + 18))
        self.font.render_to(surface, (0, 0), self.posText, self.colour, None, 0, 0, 72)

    def updatePosText(self):
        self.posText = ''.join((str(self.pos[0]/10.0), ', ', str(self.pos[1]/10.0)))
        pass

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

    def update(self, updateTime):
        if self.pos == self.targetPos:
            self.targetReached(updateTime)
        else:
            if updateTime > self.startTime + self.moveTime:
                self.targetReached(updateTime)
            else:
                timeOffset = (updateTime - self.startTime) / self.moveTime
                xPos = self.startPos[0] + ((self.targetPos[0] - self.startPos[0]) * timeOffset)
                yPos = self.startPos[1] + ((self.targetPos[1] - self.startPos[1]) * timeOffset)
                self.colour = self.tweenColours(self.startColour, self.targetColour, timeOffset)
                self.pos = (int(round(xPos)), int(round(yPos)))
        self.updatePosText()
        pass

    def targetReached(self, updateTime):
        self.pos = self.targetPos
        self.startPos = self.targetPos
        self.targetPos = (random.randrange(0, self.width), random.randrange(0, self.height))
        self.startTime = updateTime
        self.moveTime = random.randrange(2, 5)
        self.startColour = self.targetColour
        self.targetColour = self.pickNewColour()

    def tweenColours(self, startColour, endColour, progress):
        return (int(round((startColour[0] + ((endColour[0] - startColour[0]) * progress)))),int(round((startColour[1] + ((endColour[1] - startColour[1]) * progress)))),int(round((startColour[2] + ((endColour[2] - startColour[2]) * progress)))))
