""" Ship """

import text_display

import math
import pygame

class Ship:
    """A ship"""
    def __init__(self, x_pos, y_pos, displaySurface):
        self.rendering = True
        self._display_surf = displaySurface
        self.x_pos = x_pos
        self.y_pos = y_pos

        self.width = 20
        self.length = 50

        self.heading = 0

        self.speed = 0
        self.now = 0

        self.turning = 0
        self.accellerating = 0

        self.position = text_display.TextDisplay((10, 100), 230, 30)
        self.heading_display = text_display.TextDisplay((10, 150), 230, 30)

    def on_loop(self, update_time):
        """ Update loop """
        self.now += update_time

        self.heading += self.turning

        if self.heading < 0:
            self.heading += 360

        if self.heading >= 360:
            self.heading -= 360

        self.speed += self.accellerating

        if self.speed > 50:
            self.speed = 50

        if self.speed < 0:
            self.speed = 0

        if self.speed > 0:
            self.update_position()

        self.position.update_current_text(''.join((str(self.x_pos/1.0), ', ', str(self.y_pos/1.0))), (128, 128, 128))
        self.heading_display.update_current_text(str(self.heading), (128, 128, 128))

        print(self.heading)

    def on_render(self, color_key):
        """ Render event """
        background = pygame.Surface((self.width, self.length), pygame.HWSURFACE)
        background.set_colorkey(color_key)
        background.fill((128, 128, 128))

        # making a copy of the old center of the rectangle  
        old_center = (self.x_pos + (self.width // 2), self.y_pos + (self.length // 2))   

        # rotating the orignal image  
        new_image = pygame.transform.rotate(background, self.heading)  
        rect = new_image.get_rect()  
        # set the rotated rectangle to the old center  
        rect.center = old_center

        background = pygame.transform.rotate(background, self.heading)

        self._display_surf.blit(background, rect)

        self.position.draw(self._display_surf, (128, 128, 128))
        self.heading_display.draw(self._display_surf, (128, 128, 128))
        
    def key_press(self, event):
        """ user input test """
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                self.turning = 0
            if event.key == pygame.K_RIGHT:
                self.turning = 0
            if event.key == pygame.K_UP:
                self.accellerating = 0
            if event.key == pygame.K_DOWN:
                self.accellerating = 0
        
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.turning = -1
            if event.key == pygame.K_RIGHT:
                self.turning = 1
            if event.key == pygame.K_UP:
                self.accellerating = 1
            if event.key == pygame.K_DOWN:
                self.accellerating = -1

    def update_position(self):
        """ Update the ship position """
        self.x_pos += self.speed * math.sin(self.heading)
        self.y_pos += self.speed * math.cos(self.heading)
