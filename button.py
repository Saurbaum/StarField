"""Button for user interaction"""

import pygame

class Button:
    """UI button"""
    def __init__(self, pos, coordinates):
        self.pos = pos
        self.coordinates = coordinates

    def is_point_within(self, point):
        """Tests if point is inside the button"""
        position = len(self.coordinates)
        inside = False
        p1x, p1y = self.coordinates[0]

        for i in range(position + 1):
            p2x, p2y = self.coordinates[i % position]
            if point.y > min(p1y, p2y):
                if point.y <= max(p1y, p2y):
                    if point.x <= max(p1x, p2x):
                        if p1y != p2y:
                            xinters = (point.y-p1y)*(p2x-p1x)/(p2y-p1y)+p1x
                        if p1x == p2x or point.x <= xinters:
                            inside = not inside
            p1x, p1y = p2x, p2y

        return inside


    def draw(self, surface, colour):
        """ Draw the button """
        pygame.draw.polygon(surface, colour, self.coordinates)
        pygame.draw.polygon(surface, colour, self.coordinates, 1)
        