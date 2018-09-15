import sys
import pygame
from pygame.locals import *
import overlay
import stars

class StarfieldScanner:
    def __init__(self, width, height, displaySurface):
        self.rendering = True
        self._display_surf = displaySurface
        self.overlay = overlay.overlay(width, height)
        self.stars = stars.stars(width, height)
        self.now = 0
        self.regenerate_stars_trigger = 1

    def drawOverlay(self):
        self.overlay.draw(self._display_surf)

    def drawStarfield(self):
        self.stars.draw(self._display_surf)

    def on_loop(self, update_time):
        self.now += update_time
        if self.now >= self.regenerate_stars_trigger:
            self.stars.updateStarfield()
            self.now -= self.regenerate_stars_trigger

        self.overlay.on_loop(update_time)

    def on_render(self):
        self._display_surf.fill((0, 0, 0))
        self.drawStarfield()
        self.drawOverlay()
        pygame.display.update()

    def keyPress(self, key):
        if key == pygame.K_SPACE:
            self.stars.updateStarfield()