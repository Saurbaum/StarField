"""A spinning radar display"""

from collections import deque
import math
import pygame
from rotation import rotate_point, get_angle

import blip

class Radar:
    """ A radial radar display """
    def __init__(self, width, height, displaySurface, targets):
        self.rendering = True
        self._display_surf = displaySurface
        self.centre = (width//2, height//2)

        max_space = min(width, height)

        self.colour = (0, 128, 0, 255)
        self.background_colour = (0, 28, 0, 0)

        self.update_time = 0

        self.now = 0
        self.move_time = 5

        self.rotation_speed = 360.0
        self.start_angle = 0.0
        self.current_angle = self.start_angle
        self.last_angle = self.current_angle
        self.target_angle = self.start_angle + self.rotation_speed

        self.radius = int((max_space * 0.95) / 2)
        self.arm_length = self.radius

        self.arm_point = (self.centre[0], self.centre[1] - self.arm_length)
        self.start_point = self.arm_point

        self.major_ticks = deque()
        self.minor_ticks = deque()

        self.overlay_surface = pygame.Surface((width, height), pygame.HWSURFACE | pygame.SRCALPHA)
        self.prepare_overlay()
        self.blips = []

        self.targets = targets

    def prepare_overlay(self):
        """ Setup the overlay for first use """
        self.overlay_surface.fill((0, 28, 0))

        self.major_tick_reference = (
            (self.centre[0], self.centre[1] + (self.radius + 6)),
            (self.centre[0], self.centre[1] + (self.radius - 6)))
        major_tick_angle = 45
        for i in range(0, 360//major_tick_angle):
            self.create_ticks(self.major_tick_reference, self.major_ticks, i*major_tick_angle)

        self.minor_tick_reference = (
            (self.centre[0], self.centre[1] + (self.radius + 4)),
            (self.centre[0], self.centre[1] + (self.radius - 4)))
        minor_tick_angle = 11.25
        for i in range(0, int(360/minor_tick_angle)):
            self.create_ticks(self.minor_tick_reference, self.minor_ticks, i*minor_tick_angle)

        pygame.draw.circle(self.overlay_surface, (0, 0, 0, 0), self.centre, self.radius, 0)

        pygame.draw.circle(self.overlay_surface, self.colour, self.centre, self.radius, 3)
        for tick in self.major_ticks:
            pygame.draw.line(self.overlay_surface, self.colour, tick[0], tick[1], 3)

        for tick in self.minor_ticks:
            pygame.draw.line(self.overlay_surface, self.colour, tick[0], tick[1], 1)

    def create_ticks(self, reference_pos, ticks, angle):
        """ Setup the appropritate ticks marks on the edge of the radar """
        first = rotate_point(self.centre, angle, reference_pos[0])
        second = rotate_point(self.centre, angle, reference_pos[1])
        ticks.append((first, second))

    def draw_background(self, surface):
        """ Fill backgourn with colour """
        surface.fill(self.background_colour)

    def draw_blips(self, surface):
        """ Draw the blips """
        for blip in self.blips:
            blip.on_render(surface)

    def draw_overlay(self, surface):
        """ Draw the overlay """
        surface.blit(self.overlay_surface, (0, 0))
        pygame.draw.line(surface, self.colour, self.centre, self.arm_point, 3)

    def on_loop(self, update_time):
        """ Main update loop """
        self.update_time += update_time
        self.now += update_time
        progress = self.now / self.move_time

        for blip in self.blips:
            blip.on_loop(update_time)
            if blip.start_time == -1:
                self.blips.remove(blip)

        self.progress_sweep(progress)

        if progress >= 1.0:
            self.target_reached()

    def target_reached(self):
        """ Loop created reset angle to be based from 0 degrees again """
        self.start_angle = self.current_angle
        self.now = self.now - self.move_time

        if self.start_angle > 360.0:
            self.start_angle -= 360.0

        self.target_angle = self.start_angle + self.rotation_speed

    def on_render(self):
        """ Main drawing trigger """
        self.draw_background(self._display_surf)
        self.draw_blips(self._display_surf)
        self.draw_overlay(self._display_surf)

        for target in self.targets:
            target.on_render(self._display_surf, (0, 0))

        pygame.display.update()

    def key_press(self, key):
        """ Handle user input """
        if key == pygame.K_SPACE:
            # Any nessesary action here
            pass

    def progress_sweep(self, progress):
        """ Move the arm of the radar """
        angle = self.start_angle + ((self.target_angle - self.start_angle) * progress)

        while angle > 360:
            angle -= 360

        for target in self.targets:
            blip_angle = get_angle(self.centre[1] - target.pos[1], target.pos[0] - self.centre[0])

            blip_distance = math.sqrt(
                (self.centre[1] - target.pos[1]) ** 2 + (target.pos[0] - self.centre[0])**2)

            if (angle >= blip_angle > self.last_angle) and (self.radius > blip_distance):
                newBlip = blip.Blip(target.pos, self.update_time, target.strength, 4.8, self.colour, self.background_colour)
                self.blips.append(newBlip)

        self.current_angle = angle
        self.last_angle = self.current_angle
        self.arm_point = rotate_point(self.centre, self.current_angle, self.start_point)
