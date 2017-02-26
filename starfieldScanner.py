import sys
import time
from collections import deque
import pygame
from pygame.locals import *
import overlay
import stars
import ctypes

class starfieldScanner:   
    def __init__(self, width, height, displaySurface):
        self.rendering = True
        self._display_surf = displaySurface
        self.overlay = overlay.overlay(width, height)
        self.stars = stars.stars(width, height)
        self.now = time.time()

    def drawOverlay(self):
        self.overlay.draw(self._display_surf)

    def drawStarfield(self):
        self.stars.draw(self._display_surf)
         
    def on_loop(self, updateTime):
        if updateTime >= self.now + 0.5:
            self.stars.updateStarfield()
            self.now = updateTime

        self.overlay.update(updateTime)

    def on_render(self):
        self._display_surf.fill((0,0,0))
        self.drawStarfield()
        self.drawOverlay()
        pygame.display.update()

    def keyPress(self, key):
        if key == pygame.K_SPACE:
            self.stars.updateStarfield()