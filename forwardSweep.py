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

        self.colour = (0,128,0)

        self.now = 0
        self.moveTime = 3
        self.startAngle = 0
        self.currentAngle = self.startAngle
        self.rotationSpeed = 1

        self.radius = int(self.maxSpace * 0.95)
        self.armLength = self.radius
        
        self.armStartPoint = (self.centre[0], int(height*0.98)) 
        self.armPoint = (self.centre[0], self.armStartPoint[1] - self.armLength)
        self.startPoint = self.armPoint

        self.maxAngle = 0;

        self.overLaySurface = pygame.Surface((width, height), pygame.HWSURFACE)
        self.prepareOverlay()

    def prepareOverlay(self):
        width = self.centre[0]*2

        for angle in range(0,90):
            testPoint = rotatePoint(self.armStartPoint, angle, self.armPoint)
            if testPoint[0] < (width * 0.99) :
                self.maxAngle = angle

        pygame.draw.line(self.overLaySurface, self.colour, self.armStartPoint, rotatePoint(self.armStartPoint, self.maxAngle, self.armPoint), 1)
        pygame.draw.line(self.overLaySurface, self.colour, self.armStartPoint, rotatePoint(self.armStartPoint, -self.maxAngle, self.armPoint), 1)


    def on_loop(self, updateTime):
        self.now += updateTime
        progress = self.now / self.moveTime

        self.progressSweep(progress)

        if progress >= 1.0:
            self.targetReached(updateTime)

    def progressSweep(self, progress):
        pass

    def targetReached(self, updateTime):
        self.now = 0
        self.startAngle = self.currentAngle
        self.targetAngle = self.startAngle + self.rotationSpeed

        if self.targetAngle > 360.0 and self.startAngle > 360.0:
            self.targetAngle -= 360.0
            self.startAngle -= 360.0

    def drawBackground(self, surface):
        surface.fill((128,128,0))

    def drawOverlay(self, surface):
        surface.blit(self.overLaySurface, (0,0))
        pygame.draw.line(surface, self.colour, self.armStartPoint, self.armPoint, 3)


    def on_render(self):
        self.drawBackground(self._display_surf)
        self.drawOverlay(self._display_surf)       
        
        pygame.display.update()