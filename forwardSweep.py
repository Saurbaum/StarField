import math
from collections import deque
import pygame
from pygame.locals import *

class forwardSweep:   
    def __init__(self, width, height, displaySurface):
    	self._display_surf = displaySurface
    	self.now = 0
    	self.moveTime = 3
    	self.startAngle = 0
    	self.currentAngle = self.startAngle
    	self.rotationSpeed = 1

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

    def drawBackground(self, surface):
        pass

    def drawOverlay(self, surface):
        pass 

    def on_render(self):
        self.drawBackground(self._display_surf)
        self.drawOverlay(self._display_surf)       
        
        pygame.display.update()