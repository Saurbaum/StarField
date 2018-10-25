"""Provides a feild of randomly generated stars"""

import random
import pygame

class stars(object):
    """Provides a feild of randomly generated stars"""
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.starSurface = pygame.Surface((width, height), pygame.HWSURFACE)
        self.update_starfield()

    def draw(self, surface):
        """Reder stars to provided surface"""
        surface.blit(self.starSurface, (0, 0))

    def pickColour(self):
        """Pick a colour for the stars"""
        colour = random.randrange(0, 7)
        if colour == 0: # Red
            blue_tint = random.randrange(50, 128)
            return (random.randrange(200, 255), blue_tint, blue_tint)
        if colour == 1: # Blue
            return (random.randrange(220, 255), random.randrange(220, 255), random.randrange(220, 255))
        if colour == 2: # Orange
            orange = random.randrange(200, 255)
            return (orange, orange, random.randrange(50, 128))    
        if colour == 3: # Purple
            purple = random.randrange(200, 255)
            return (purple, random.randrange(50, 128), purple)   
            
        # White
        light_tint = random.randrange(200, 255) 
        return (200, light_tint, light_tint)

    def update_starfield(self):
        """Update stars"""
        self.starSurface.fill((0 ,0, 0))
        for _ in range(0, 40):
            pygame.draw.circle(self.starSurface, self.pickColour(), (random.randrange(0, self.width), random.randrange(0, self.height)), random.randrange(1, 7, 2), 0)
