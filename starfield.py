import sys
from collections import deque
import pygame
from pygame.locals import *
import starfieldScanner
import radar
import ctypes

class App:
    def __init__(self):
        self._running = True
        self._display_surf = None
        self.activeDisplay = None
        self.clock = pygame.time.Clock()

    def on_init(self):
        pygame.init()
        pygame.mouse.set_visible(False)

        if sys.platform.startswith("win32"):
            ctypes.windll.user32.SetProcessDPIAware()

        self.now = 0

        width, height = pygame.display.Info().current_w, pygame.display.Info().current_h
        self._display_surf = pygame.display.set_mode((width, height), pygame.FULLSCREEN | pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._running = True

        self.starfieldScanner = starfieldScanner.starfieldScanner(width, height, self._display_surf)
        self.radar = radar.radar(width, height, self._display_surf)
        self.activeDisplay = self.starfieldScanner

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False            
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_ESCAPE:
                self._running = False
            elif event.key == pygame.K_1:
                self.activeDisplay = self.starfieldScanner;
            elif event.key == pygame.K_2:
                self.activeDisplay = self.radar;
            else:
                self.activeDisplay.keyPress(event.key)
    
    def on_loop(self):
        self.now = self.clock.get_rawtime() / 1000
        self.starfieldScanner.on_loop(self.now)
        self.radar.on_loop(self.now)
 
    def on_render(self):
        self.activeDisplay.on_render()
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
            self.clock.tick(60)

        self.on_cleanup()

if __name__ == "__main__" :
    theApp = App()
    theApp.on_execute()
