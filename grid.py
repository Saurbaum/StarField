import pygame

class grid:
    def __init__(self, width, height, step, colour):
        self.colour = colour
        self.width = width
        self.height = height
        self.step = step
        self.steps = int(self.width/self.step)
        
    def draw(self, surface):
        pos = 0;
        
        for i in range(0, self.steps):
            pos += self.step
            pygame.draw.line(surface, self.colour, (0, pos), (self.width, pos))
            pygame.draw.line(surface, self.colour, (pos, 0), (pos, self.height))        