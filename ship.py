""" Ship """

import pygame

class Ship:
    """A gauges"""
    def __init__(self, x_pos, y_pos, displaySurface):
        self.rendering = True
        self._display_surf = displaySurface
        self.x_pos = x_pos
        self.y_pos = y_pos

        self.width = 20
        self.length = 50

        self.heading = 0

        self.speed = 0

        self.turning = 0

        self.center = (self.x_pos + (self.width // 2), self.y_pos + (self.length // 2))  

    def on_loop(self, update_time):
        """ Update loop """
        self.now += update_time

        self.heading += self.turning

        if self.heading < 0:
            self.heading += 360

        if self.heading > 360:
            self.heading -= 360

        print(self.heading)

    def on_render(self, color_key):
        """ Render event """
        background = pygame.Surface((self.width, self.length), pygame.HWSURFACE)
        background.set_colorkey(color_key)
        background.fill((128, 128, 128))

        # making a copy of the old center of the rectangle  
        old_center = self.center  

        # rotating the orignal image  
        new_image = pygame.transform.rotate(background, self.heading)  
        rect = new_image.get_rect()  
        # set the rotated rectangle to the old center  
        rect.center = old_center

        background = pygame.transform.rotate(background, self.heading)

        self._display_surf.blit(background, rect)
        
    def key_press(self, event):
        """ user input test """
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                self.turning = 0
            if event.key == pygame.K_RIGHT:
                self.turning = 0
        
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.turning = -1
            if event.key == pygame.K_RIGHT:
                self.turning = 1
