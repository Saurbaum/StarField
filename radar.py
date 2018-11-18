"""A spinning radar display"""

from collections import deque
import math
import pygame
from rotation import rotate_point, get_angle
from tweenColours import tweenColours

class radar:
    """ A radial radar display """
    def __init__(self, width, height, displaySurface, blip):
        self.rendering = True
        self._display_surf = displaySurface
        self.centre = (width//2, height//2)

        max_space = min(width, height)

        self.colour = (0, 128, 0)
        self.background_colour = (0, 28, 0)

        self.updateTime = 0

        self.now = 0
        self.moveTime = 5

        self.rotationSpeed = 360.0
        self.startAngle = 0.0
        self.currentAngle = self.startAngle
        self.lastAngle = self.currentAngle
        self.targetAngle = self.startAngle + self.rotationSpeed

        self.radius = int((max_space * 0.95) / 2)
        self.armLength = self.radius

        self.armPoint = (self.centre[0], self.centre[1] - self.armLength)
        self.startPoint = self.armPoint

        self.majorTicks = deque()
        self.minorTicks = deque()

        self.overLaySurface = pygame.Surface((width, height), pygame.HWSURFACE | pygame.SRCALPHA)
        self.prepareOverlay()

        self.blip = blip
        self.blipRenderPos = (0, 0)
        self.blipFadeTime = 4.8
        self.blipStartTime = -1

    def prepareOverlay(self):
        self.overLaySurface.fill((0, 28, 0))

        self.majorTickReference = (
            (self.centre[0], self.centre[1] + (self.radius + 6)),
            (self.centre[0], self.centre[1] + (self.radius - 6)))
        majorTickAngle = 45
        for i in range(0, 360//majorTickAngle):
            self.createTicks(self.majorTickReference, self.majorTicks, i*majorTickAngle)

        self.minorTickReference = (
            (self.centre[0], self.centre[1] + (self.radius + 4)),
            (self.centre[0], self.centre[1] + (self.radius - 4)))
        minorTickAngle = 11.25
        for i in range(0, int(360/minorTickAngle)):
            self.createTicks(self.minorTickReference, self.minorTicks, i*minorTickAngle)

        pygame.draw.circle(self.overLaySurface, (0, 0 ,0, 0), self.centre, self.radius, 0)

        pygame.draw.circle(self.overLaySurface, self.colour, self.centre, self.radius, 3)
        for tick in self.majorTicks:
            pygame.draw.line(self.overLaySurface, self.colour, tick[0], tick[1], 3)

        for tick in self.minorTicks:
            pygame.draw.line(self.overLaySurface, self.colour, tick[0], tick[1], 1)

    def createTicks(self, referencePos, ticks, angle):
        first = rotate_point(self.centre, angle, referencePos[0])
        second = rotate_point(self.centre, angle, referencePos[1])
        ticks.append((first, second))

    def drawBackground(self, surface):
        surface.fill(self.background_colour)

    def drawBlip(self, surface):
        if self.blipStartTime == -1:
            return

        progress = (self.updateTime - self.blipStartTime) / self.blipFadeTime

        if progress >= 1.0 or progress < 0:
            self.blipStartTime = -1
            return

        steps = int(self.blip.strength * (1 - progress))

        for size in range(steps):
            value = self.blip.strength - size
            timeOffset = (value) / self.blip.strength
            pygame.draw.circle(surface, tweenColours(self.colour, self.background_colour, timeOffset), self.blipRenderPos, value)

    def drawOverlay(self, surface):
        surface.blit(self.overLaySurface, (0,0))
        pygame.draw.line(surface, self.colour, self.centre, self.armPoint, 3)

    def on_loop(self, updateTime):
        self.updateTime += updateTime
        self.now += updateTime
        progress = self.now / self.moveTime

        if progress >= 1.0:
            self.progressSweep(1.0)
            self.targetReached(updateTime)
        else:
            self.progressSweep(progress)

    def targetReached(self, updateTime):
        self.now = 0
        self.startAngle = self.currentAngle

        if self.startAngle > 360.0:
            self.startAngle -= 360.0

        self.targetAngle = self.startAngle + self.rotationSpeed

    def on_render(self):
        self.drawBackground(self._display_surf)
        self.drawBlip(self._display_surf)
        self.drawOverlay(self._display_surf)   

        pygame.display.update()

    def key_press(self, key):
        if key == pygame.K_SPACE:
            # Any nessesary action here
            pass

    def progressSweep(self, progress):
        angle = self.startAngle + ((self.targetAngle - self.startAngle) * progress)

        if angle > 360:
            angle -= 360

        blip_angle = get_angle(self.centre[1] - self.blip.pos[1], self.blip.pos[0] - self.centre[0])

        blip_distance = math.sqrt(
            (self.centre[1] - self.blip.pos[1]) ** 2 + (self.blip.pos[0] - self.centre[0])**2) 

        if (angle >= blip_angle > self.lastAngle) and (self.radius > blip_distance):
            self.blipRenderPos = (self.blip.pos[0], self.blip.pos[1])
            self.blipStartTime = self.updateTime

        self.currentAngle = angle
        self.lastAngle = self.currentAngle
        self.armPoint = rotate_point(self.centre, self.currentAngle, self.startPoint)
