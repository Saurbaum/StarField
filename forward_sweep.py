"""A forward facing radar display"""

import pygame
from rotation import rotate_point

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
        self.prepare_overlay()

        self.start_angle = -self.max_angle
        self.current_angle = self.start_angle
        self.target_angle = self.max_angle

    def prepare_overlay(self):
        """Setup the overlay for the display"""
        width = self.centre[0]*2

        for angle in range(0, 90):
            test_point = rotate_point(self.arm_start_point, angle, self.arm_point)
            if test_point[0] < (width * 0.99):
                self.max_angle = angle

        self.overlay_surface.fill((0, 28, 0, 0))
        pygame.draw.line(
            self.overlay_surface, self.colour, self.arm_start_point, rotate_point(
                self.arm_start_point, self.max_angle, self.arm_point), 1)
        pygame.draw.line(
            self.overlay_surface, self.colour, self.arm_start_point, rotate_point(
                self.arm_start_point, -self.max_angle, self.arm_point), 1)

    def on_loop(self, update_time):
        """Main update loop"""
        self.now += update_time
        progress = self.now / self.move_time

        if progress >= 1.0:
            self.progress_sweep(1.0)
            self.target_reached()
        else:
            self.progress_sweep(progress)

    def progress_sweep(self, progress):
        """Update the sweep arm"""
        angle = self.start_angle + ((self.target_angle - self.start_angle) * progress)
        self.current_angle = angle

        self.arm_point = rotate_point(self.arm_start_point, self.current_angle, self.start_point)

    def target_reached(self):
        """Arm reached the target position"""
        self.now = 0
        self.start_angle = self.current_angle
        self.target_angle = self.start_angle * -1

    def draw_background(self, surface):
        """Draw the background"""
        surface.fill((0, 32, 0))

    def draw_overlay(self, surface):
        """Draw overlay"""
        surface.blit(self.overlay_surface, (0, 0))
        pygame.draw.line(surface, self.arm_colour, self.arm_start_point, self.arm_point, 3)

    def key_press(self, key):
        """Handle the key press"""
        if key == pygame.K_SPACE:
            # Any nessesary action here
            pass

    def on_render(self):
        self.draw_background(self._display_surf)
        self.draw_overlay(self._display_surf)       

        pygame.display.update()
