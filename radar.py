import sys
import math
from collections import deque
import pygame
from pygame.locals import *
import overlay
import stars
import ctypes

class radar:   
    def __init__(self, width, height, displaySurface):
        self.rendering = True
        self._display_surf = displaySurface
        self.centre = (width//2, height//2)

        maxSpace = min(width, height)

        self.colour = (0,128,0)

        self.now = 0
        self.moveTime = 5

        self.rotationSpeed = 360.0
        self.startAngle = 0.0
        self.currentAngle = self.startAngle
        self.targetAngle = self.startAngle + self.rotationSpeed
        
        self.radius = int((maxSpace * 0.95) / 2)
        self.armLength = self.radius
        
        self.armPoint = (self.centre[0], self.centre[1] - self.armLength)
        self.startPoint = self.armPoint

        self.majorTicks = deque()
        self.minorTicks = deque()

        self.overLaySurface = pygame.Surface((width, height), pygame.HWSURFACE)
        self.prepareOverlay()

    def prepareOverlay(self):
        self.majorTickReference = ((self.centre[0], self.centre[1] + (self.radius + 6)),(self.centre[0], self.centre[1] + (self.radius - 6)))
        majorTickAngle = 45
        for i in range(0, 360//majorTickAngle):
            self.createTicks(self.majorTickReference, self.majorTicks, i*majorTickAngle)

        self.minorTickReference = ((self.centre[0], self.centre[1] + (self.radius + 4)),(self.centre[0], self.centre[1] + (self.radius - 4)))
        minorTickAngle = 11.25
        for i in range(0, int(360/minorTickAngle)):
            self.createTicks(self.minorTickReference, self.minorTicks, i*minorTickAngle)

        pygame.draw.circle(self.overLaySurface, self.colour, self.centre, self.radius, 3)
        for tick in self.majorTicks:
            pygame.draw.line(self.overLaySurface, self.colour, tick[0], tick[1], 3)

        for tick in self.minorTicks:
            pygame.draw.line(self.overLaySurface, self.colour, tick[0], tick[1], 1)


    def createTicks(self, referencePos, ticks, angle):
        first = self.rotatePoint(self.centre, angle, referencePos[0])
        second = self.rotatePoint(self.centre, angle, referencePos[1])
        ticks.append((first, second))

    def drawBackground(self, surface):
        surface.fill((0,28,0))

    def drawOverlay(self, surface):
        surface.blit(self.overLaySurface, (0,0))
        pygame.draw.line(surface, self.colour, self.centre, self.armPoint, 3)

    def on_loop(self, updateTime):
        self.now += updateTime
        progress = self.now / self.moveTime

        self.progressSweep(progress)

        if progress >= 1.0:
            self.targetReached(updateTime)

    def targetReached(self, updateTime):
        self.now = 0
        self.startAngle = self.currentAngle
        self.targetAngle = self.startAngle + self.rotationSpeed

        if self.targetAngle > 360.0 and self.startAngle > 360.0:
            self.targetAngle -= 360.0
            self.startAngle -= 360.0

    def on_render(self):
        self.drawBackground(self._display_surf)
        self.drawOverlay(self._display_surf)       
        
        pygame.display.update()

    def keyPress(self, key):
        if key == pygame.K_SPACE:
            # Any nessesary action here
            pass

    def progressSweep(self, progress):
        angle = self.startAngle + ((self.targetAngle - self.startAngle) * progress)
        self.currentAngle = angle
        self.armPoint = self.rotatePoint(self.centre, self.currentAngle, self.startPoint)
    
    def rotatePoint(self, offset, angle, point):
        s = math.sin(math.radians(angle))
        c = math.cos(math.radians(angle))

        # Translate point back to origin:
        x = point[0] - offset[0]
        y = point[1] - offset[1]

        # Rotate point
        xNew = x * c - y * s
        yNew = x * s + y * c

        # Translate point back:
        return (xNew + offset[0], yNew + offset[1]);

