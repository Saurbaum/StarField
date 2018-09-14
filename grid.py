import pygame

class grid:
    def __init__(self, width, height, step):
        self.width = width
        self.height = height
        self.step = step
        self.horizontalSteps = self.width//self.step
        self.verticalSteps = self.height//self.step
        
    def draw(self, surface, colour):
        pygame.draw.rect(surface, colour, (0, 0, self.width, self.height), 1)

        pos = self.step
        
        for _i in range(self.horizontalSteps):
            pygame.draw.line(surface, colour, (pos, 0), (pos, self.height))        
            pos += self.step

        pos = self.step
        for _i in range(self.verticalSteps):
            pygame.draw.line(surface, colour, (0, pos), (self.width, pos))
            pos += self.step