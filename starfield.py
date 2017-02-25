import sys
import time
from collections import deque
import pygame
from pygame.locals import *
import overlay
import stars
import ctypes

class App:
    def __init__(self):
        self._running = True
        self._display_surf = None
        
    def drawOverlay(self):
        self.overlay.draw(self._display_surf)

    def drawStarfield(self):
        self.stars.draw(self._display_surf)
        
    def on_init(self):
        pygame.init()
        pygame.mouse.set_visible(False)

        if sys.platform.startswith("win32"):
            user32 = ctypes.windll.user32
            user32.SetProcessDPIAware()

        width, height = pygame.display.Info().current_w, pygame.display.Info().current_h
        self._display_surf = pygame.display.set_mode((width, height), pygame.FULLSCREEN | pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._running = True
        self.now = time.time()
        self.overlay = overlay.overlay(width, height)
        self.stars = stars.stars(width, height)

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False            
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_ESCAPE:
                self._running = False
            if event.key == pygame.K_SPACE:
                self.stars.updateStarfield()
    
    def on_loop(self):
        if time.time() >= self.now + 0.5:
            self.stars.updateStarfield()
            self.now = time.time()

        self.overlay.update(time.time())

    def on_render(self):
        self._display_surf.fill((0,0,0))
        self.drawStarfield()
        self.drawOverlay()
        pygame.display.update()

    def on_cleanup(self):
        pygame.quit()

    def on_execute(self):
        self.on_init()

        while( self._running ):
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
        self.on_cleanup()

if __name__ == "__main__" :
    theApp = App()
    theApp.on_execute()
