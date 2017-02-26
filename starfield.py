import sys
import time
from collections import deque
import pygame
from pygame.locals import *
import starfieldScanner
import ctypes

class App:
    def __init__(self):
        self._running = True
        self._display_surf = None

    def on_init(self):
        pygame.init()
        pygame.mouse.set_visible(False)

        if sys.platform.startswith("win32"):
            ctypes.windll.user32.SetProcessDPIAware()

        self.now = time.time()

        width, height = pygame.display.Info().current_w, pygame.display.Info().current_h
        self._display_surf = pygame.display.set_mode((width, height), pygame.FULLSCREEN | pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._running = True

        self.starfieldScanner = starfieldScanner.starfieldScanner(width, height, self._display_surf)

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False            
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_ESCAPE:
                self._running = False
            else:
                self.starfieldScanner.keyPress(event.key)
    
    def on_loop(self):
        self.starfieldScanner.on_loop(time.time())
 
    def on_render(self):
        self._display_surf.fill((0,0,0))
        self.starfieldScanner.on_render()
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
