import math
from collections import deque
import pygame
from pygame.locals import *
from rotation import *

class forwardSweep:   
    def __init__(self, width, height, displaySurface):
        self._display_surf = displaySurface

        self.centre = (width//2, height//2)

        self.maxSpace = min(width, height)

        self.colour = (0,255,0)
        self.armColour = (0,128,0)

        self.now = 0
        self.moveTime = 5
        self.startAngle = 0

        self.radius = int(self.maxSpace * 0.95)
        self.armLength = self.radius
        
        self.armStartPoint = (self.centre[0], int(height*0.98)) 
        self.armPoint = (self.centre[0], self.armStartPoint[1] - self.armLength)
        self.startPoint = self.armPoint

        self.maxAngle = 0;

        self.overLaySurface = pygame.Surface((width, height), pygame.HWSURFACE | pygame.SRCALPHA)
        self.prepareOverlay()

        self.startAngle = -self.maxAngle
        self.currentAngle = self.startAngle
        self.targetAngle = self.maxAngle

    def prepareOverlay(self):
        width = self.centre[0]*2

        for angle in range(0,90):
            testPoint = rotatePoint(self.armStartPoint, angle, self.armPoint)
            if testPoint[0] < (width * 0.99) :
                self.maxAngle = angle

        self.overLaySurface.fill((0,28,0,0))
        pygame.draw.line(self.overLaySurface, self.colour, self.armStartPoint, rotatePoint(self.armStartPoint, self.maxAngle, self.armPoint), 1)
        pygame.draw.line(self.overLaySurface, self.colour, self.armStartPoint, rotatePoint(self.armStartPoint, -self.maxAngle, self.armPoint), 1)

    def on_loop(self, updateTime):
        self.now += updateTime
        progress = self.now / self.moveTime

        if progress >= 1.0:
            self.progressSweep(1.0)
            self.targetReached(updateTime)
        else:
            self.progressSweep(progress)


    def progressSweep(self, progress):
        angle = self.startAngle + ((self.targetAngle - self.startAngle) * progress)
        self.currentAngle = angle

        self.armPoint = rotatePoint(self.armStartPoint, self.currentAngle, self.startPoint)

    def targetReached(self, updateTime):
        self.now = 0
        self.startAngle = self.currentAngle
        self.targetAngle = self.startAngle * -1

    def drawBackground(self, surface):
        surface.fill((0,32,0))

    def drawOverlay(self, surface):
        surface.blit(self.overLaySurface, (0,0))
        pygame.draw.line(surface, self.armColour, self.armStartPoint, self.armPoint, 3)

    def keyPress(self, key):
        if key == pygame.K_SPACE:
            # Any nessesary action here
            pass

    def on_render(self):
        self.drawBackground(self._display_surf)
        self.drawOverlay(self._display_surf)       
        
        pygame.display.update()