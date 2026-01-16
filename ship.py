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

        screen_width = self._display_surf.get_width()
        screen_height = self._display_surf.get_height()

        # rotating the original image (negate heading to match clockwise rotation)
        rotated_image = pygame.transform.rotate(background, -self.heading)

        # List of positions to draw (original + wrapped positions)
        positions = [(self.x_pos, self.y_pos)]
        
        # Add wrapped positions if ship is near edges
        if self.x_pos > screen_width - self.width:
            positions.append((self.x_pos - screen_width, self.y_pos))
        if self.x_pos < self.width:
            positions.append((self.x_pos + screen_width, self.y_pos))
        if self.y_pos > screen_height - self.length:
            positions.append((self.x_pos, self.y_pos - screen_height))
        if self.y_pos < self.length:
            positions.append((self.x_pos, self.y_pos + screen_height))
        
        # Draw ship at each position
        for x, y in positions:
            old_center = (x + (self.width // 2), y + (self.length // 2))
            rect = rotated_image.get_rect()
            rect.center = old_center
            self._display_surf.blit(rotated_image, rect)

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
        # Convert heading (0° = up) to radians
        radians = math.radians(self.heading)
        self.x_pos += self.speed * math.sin(radians)
        self.y_pos -= self.speed * math.cos(radians)
        
        # Wrap around screen edges
        # You'll need to get the screen width and height
        screen_width = self._display_surf.get_width()
        screen_height = self._display_surf.get_height()
        
        if self.x_pos > screen_width:
            self.x_pos = -self.width
        elif self.x_pos < -self.width:
            self.x_pos = screen_width
    
        if self.y_pos > screen_height:
            self.y_pos = -self.length
        elif self.y_pos < -self.length:
            self.y_pos = screen_height
