import sys
import time
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

        self.startTime = time.time()
        self.moveTime = 5

        self.rotationSpeed = 360.0
        self.startAngle = 0.0
        self.currentAngle = self.startAngle
        self.targetAngle = self.startAngle + self.rotationSpeed
        
        self.radius = int((maxSpace * 0.95) / 2)
        self.armLength = self.radius
        
        self.armPoint = (self.centre[0], self.centre[1] - self.armLength)
        self.startPoint = self.armPoint

        self.now = time.time()

    def drawBackground(self, surface):
        surface.fill((0,32,0))

    def drawOverlay(self, surface):
        pygame.draw.circle(surface, self.colour, self.centre, self.radius, 3)
        pygame.draw.line(surface, self.colour, self.centre, self.armPoint, 3)

    def on_loop(self, updateTime):
        progress = (updateTime - self.startTime) / self.moveTime

        self.progressSweep(progress)

        if progress >= 1.0:
            self.targetReached(updateTime)

    def targetReached(self, updateTime):
        self.startAngle = self.currentAngle
        self.targetAngle = self.startAngle + self.rotationSpeed

        if self.targetAngle > 360.0 and self.startAngle > 360.0:
            self.targetAngle -= 360.0
            self.startAngle -= 360.0

        self.startTime = updateTime

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

