import random
import time
from collections import deque
import pygame
from pygame.locals import *

class App:
    def __init__(self):
        self._running = True
        self._display_surf = None
        self.overlayColour = (0, 255, 0)
        self.overlayPos = (50, 50)
        self.overlayTargetPos = (50, 50)
        self.overlayStartPos = (50, 50)
        self.overlayMoveTime = 5

    def pickColour(self):
        colour = random.randrange(0,5)
        if colour == 0: # Red
            blueTint = random.randrange(50,128)
            return (random.randrange(200,255), blueTint, blueTint)
        if colour == 1: # Blue
            return (random.randrange(220, 255), random.randrange(220,255), random.randrange(220, 255))
            
        # White
        lightTint = random.randrange(200,255) 
        return (200, lightTint, lightTint)

    def drawOverlay(self):
        pygame.draw.line(self._display_surf, self.overlayColour, (0, self.overlayPos[1]), (self.width, self.overlayPos[1]))
        pygame.draw.line(self._display_surf, self.overlayColour, (self.overlayPos[0], 0), (self.overlayPos[0], self.height))
        pygame.draw.circle(self._display_surf, self.overlayColour, self.overlayPos, 20, 1)
        pygame.draw.line(self._display_surf, self.overlayColour, (self.overlayPos[0] - 10, self.overlayPos[1] - 10), (self.overlayPos[0] - 18, self.overlayPos[1] - 18))
        pygame.draw.line(self._display_surf, self.overlayColour, (self.overlayPos[0] + 10, self.overlayPos[1] - 10), (self.overlayPos[0] + 18, self.overlayPos[1] - 18))
        pygame.draw.line(self._display_surf, self.overlayColour, (self.overlayPos[0] + 10, self.overlayPos[1] + 10), (self.overlayPos[0] + 18, self.overlayPos[1] + 18))
        pygame.draw.line(self._display_surf, self.overlayColour, (self.overlayPos[0] - 10, self.overlayPos[1] + 10), (self.overlayPos[0] - 18, self.overlayPos[1] + 18))

    def drawStarfield(self):
        self._display_surf.fill((0,0,0))
        for star in self.stars:
            pygame.draw.circle(self._display_surf, star[0], star[1], star[2], 0)

    def updateStarfield(self):
        tempDeque = deque()
        for i in range(0, 40):
            tempDeque.append((self.pickColour(), (random.randrange(0,self.width), random.randrange(0,self.height)), random.randrange(1,5,2)))
        return tempDeque

    def on_init(self):
        random.seed(3)
        pygame.init()
        pygame.mouse.set_visible(False)
        self.size = self.width, self.height = pygame.display.Info().current_w, pygame.display.Info().current_h
        self._display_surf = pygame.display.set_mode(self.size, pygame.FULLSCREEN | pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._running = True
        self.now = time.time()
        self.stars = self.updateStarfield()

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False            
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_ESCAPE:
                self._running = False
            if event.key == pygame.K_SPACE:
                self.updateStarfield()
    
    def on_loop(self):
        if time.time() >= self.now + 0.5:
            self.stars = self.updateStarfield()
            self.now = time.time()

        if self.overlayPos == self.overlayTargetPos:
            self.overlayStartPos = self.overlayTargetPos
            self.overlayTargetPos = (random.randrange(0, self.width), random.randrange(0, self.height))
            self.overlayStartTime = time.time()
        else:
            if time.time() > self.overlayStartTime + self.overlayMoveTime:
                self.overlayPos = self.overlayTargetPos
                self.overlayPos = self.overlayTargetPos
            else:
                timeOffset = (time.time() - self.overlayStartTime) / self.overlayMoveTime
                xPos = self.overlayStartPos[0] + ((self.overlayTargetPos[0] - self.overlayStartPos[0]) * timeOffset)
                yPos = self.overlayStartPos[1] + ((self.overlayTargetPos[1] - self.overlayStartPos[1]) * timeOffset)
                self.overlayPos = (int(round(xPos)), int(round(yPos)))
        pass

    def on_render(self):
        self.drawStarfield()
        self.drawOverlay()
        pygame.display.update()
        pass

    def on_cleanup(self):
        pygame.quit()

    def on_execute(self):
        if self.on_init() == False:
            self._running = False

        while( self._running ):
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
        self.on_cleanup()

if __name__ == "__main__" :
    theApp = App()
    theApp.on_execute()
