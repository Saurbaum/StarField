import pygame

class button:
    def __init__(self, pos, coordinates):
        self.pos = pos
        self.coordinates = coordinates
        pass

    def isPointWithin(self, point):
        n = len(self.coordinates)
        inside = False
        p1x,p1y = self.coordinates[0]
        
        for i in range(n+1):
            p2x,p2y = self.coordinates[i % n]
            if y > min(p1y,p2y):
                if y <= max(p1y,p2y):
                    if x <= max(p1x,p2x):
                        if p1y != p2y:
                            xinters = (y-p1y)*(p2x-p1x)/(p2y-p1y)+p1x
                        if p1x == p2x or x <= xinters:
                            inside = not inside
            p1x,p1y = p2x,p2y

        return inside


    def draw(self, surface, colour):
        pygame.draw.polygon(surface, colour, self.coordinates)
        pygame.draw.polygon(surface, colour, self.coordinates, 1)
        pass