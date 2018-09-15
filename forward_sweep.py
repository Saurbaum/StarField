"""A forward facing radar display"""

import pygame
from rotation import rotatePoint

class ForwardSweep:
    """A forward facing radar display"""

    def __init__(self, width, height, displaySurface):
        self._display_surf = displaySurface

        self.centre = (width//2, height//2)

        self.max_space = min(width, height)

        self.colour = (0, 255, 0)
        self.arm_colour = (0, 128, 0)

        self.now = 0
        self.move_time = 5

        self.radius = int(self.max_space * 0.95)
        self.arm_length = self.radius

        self.arm_start_point = (self.centre[0], int(height * 0.98))
        self.arm_point = (self.centre[0], self.arm_start_point[1] - self.arm_length)
        self.start_point = self.arm_point

        self.max_angle = 0

        self.overlay_surface = pygame.Surface((width, height), pygame.HWSURFACE | pygame.SRCALPHA)
        self.prepareOverlay()

        self.start_angle = -self.max_angle
        self.currentAngle = self.start_angle
        self.targetAngle = self.max_angle

    def prepareOverlay(self):
        width = self.centre[0]*2

        for angle in range(0, 90):
            test_point = rotatePoint(self.arm_start_point, angle, self.arm_point)
            if test_point[0] < (width * 0.99):
                self.max_angle = angle

        self.overlay_surface.fill((0, 28, 0, 0))
        pygame.draw.line(
            self.overlay_surface, self.colour, self.arm_start_point, rotatePoint(
                self.arm_start_point, self.max_angle, self.arm_point), 1)
        pygame.draw.line(
            self.overlay_surface, self.colour, self.arm_start_point, rotatePoint(
                self.arm_start_point, -self.max_angle, self.arm_point), 1)

    def on_loop(self, update_time):
        self.now += update_time
        progress = self.now / self.move_time

        if progress >= 1.0:
            self.progressSweep(1.0)
            self.targetReached()
        else:
            self.progressSweep(progress)

    def progressSweep(self, progress):
        angle = self.start_angle + ((self.targetAngle - self.start_angle) * progress)
        self.currentAngle = angle

        self.arm_point = rotatePoint(self.arm_start_point, self.currentAngle, self.start_point)

    def targetReached(self):
        self.now = 0
        self.start_angle = self.currentAngle
        self.targetAngle = self.start_angle * -1

    def drawBackground(self, surface):
        surface.fill((0, 32, 0))

    def drawOverlay(self, surface):
        surface.blit(self.overlay_surface, (0, 0))
        pygame.draw.line(surface, self.arm_colour, self.arm_start_point, self.arm_point, 3)

    def keyPress(self, key):
        if key == pygame.K_SPACE:
            # Any nessesary action here
            pass

    def on_render(self):
        self.drawBackground(self._display_surf)
        self.drawOverlay(self._display_surf)       

        pygame.display.update()
