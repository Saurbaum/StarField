import pygame

class grid:
    def __init__(self, width, height, step):
        self.width = width
        self.height = height
        self.step = step
        self.steps = self.width//self.step
        
    def draw(self, surface, colour):
        pos = 0
        
        for i in range(self.steps):
            pos += self.step
            pygame.draw.line(surface, colour, (0, pos), (self.width, pos))
            pygame.draw.line(surface, colour, (pos, 0), (pos, self.height))        