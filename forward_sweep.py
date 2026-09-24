"""A forward facing radar display"""

import math
import pygame
import blip
from rotation import rotate_point

class ForwardSweep:
    """A forward facing radar display"""

    def __init__(self, width, height, displaySurface, targets, range, direction):
        self._display_surf = displaySurface

        self.centre = (width//2, height//2)

        self.max_space = min(width, height)

        self.colour = (0, 255, 0, 255)
        self.arm_colour = (0, 128, 0)

        self.now = 0
        self.move_time = 5

        self.radius = int(self.max_space * 0.95)
        self.arm_length = self.radius

        self.arm_start_point = (self.centre[0], int(height * 0.98))
        self.arm_point = (self.centre[0], self.arm_start_point[1] - self.arm_length)
        self.start_point = self.arm_point

        self.max_angle = 0

        self.height = height

        self.overlay_surface = pygame.Surface((width, height), pygame.HWSURFACE | pygame.SRCALPHA)
        self.prepare_overlay()

        self.start_angle = -self.max_angle
        self.current_angle = self.start_angle
        self.last_angle = self.start_angle
        self.target_angle = self.max_angle

        self.targets = targets
        self.blips = []
        self.update_time = 0
        self.range = range
        self.direction = direction

        self.origin = (width / 2, height / 2)

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
        self.update_time += update_time
        self.now += update_time
        progress = self.now / self.move_time

        for current_blip in self.blips:
            current_blip.on_loop(update_time)

        self.blips = [current_blip for current_blip in self.blips
                      if current_blip.start_time != -1]

        if progress >= 1.0:
            self.progress_sweep(1.0)
            self.target_reached()
        else:
            self.progress_sweep(progress)

    def key_press(self, evevnt):
        """Handle the key press"""
        # if event.key == pygame.K_SPACE:
            # Any nessesary action here

    def progress_sweep(self, progress):
        """Update the sweep arm"""
        angle = self.start_angle + ((self.target_angle - self.start_angle) * progress)

        for target in self.targets:
            position = self.position_in_view(target.pos)
            if position is None:
                continue

            distance_from_origin = math.hypot(
                position[0] - self.arm_start_point[0],
                position[1] - self.arm_start_point[1])
            if distance_from_origin > self.arm_length:
                continue

            target_angle = math.degrees(math.atan2(
                position[0] - self.arm_start_point[0],
                self.arm_start_point[1] - position[1]))

            if self.sweep_crossed(target_angle, angle):
                self.blips.append(blip.Blip(
                    position, self.update_time, target.strength, 4.8,
                    self.colour, (0, 32, 0, 0)))

        self.current_angle = angle
        self.last_angle = angle

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

    def draw_blips(self, surface):
        """Draw the fading highlights created by the sweep."""
        for current_blip in self.blips:
            current_blip.on_render(surface)

    def on_render(self):
        """ The drawing trigger """
        self.draw_background(self._display_surf)

        # for target in self.targets:
        #    position = self.position_in_view(target.pos)
        #    if position is not None:
        #        target.on_render(self._display_surf, position)

        self.draw_blips(self._display_surf)
        self.draw_overlay(self._display_surf)

        pygame.display.update()

    def is_in_view(self, position):
        """Return whether a world position is inside the forward view."""
        return self.position_in_view(position) is not None

    def sweep_crossed(self, target_angle, angle):
        """Return whether the arm crossed a target since the last update."""
        if angle == self.last_angle:
            return False

        sweep_start = min(self.last_angle, angle)
        sweep_end = max(self.last_angle, angle)
        return sweep_start < target_angle <= sweep_end

    def position_in_view(self, position):
        """Convert a world position to coordinates in this display.

        The forward view starts at the centre of the world display and looks
        upward. Keep the lateral offset from the centre and map the visible
        depth range onto the full display height.
        """
        depth = self.origin[1] - position[1]
        if depth <= 0 or depth > self.range:
            return None

        x_position = self.origin[0] + (position[0] - self.origin[0])
        y_position = self.height - (depth * self.height / self.range)
        return (int(round(x_position)), int(round(y_position)))