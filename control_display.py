""" Control display """

import pygame
import gauge

class ControlDisplay:
    """A panel of gauges"""
    def __init__(self, width, height, displaySurface):
        self.rendering = True
        self._display_surf = displaySurface
        self.now = 0
        self.gauges = []
        self.gauges.append(gauge.Gauge(10, 40, 50, 50, 100, gauge.Gague_Type.UP, self._display_surf))
        self.gauges.append(gauge.Gauge(70, 40, 50, 150, 100, gauge.Gague_Type.DOWN, self._display_surf))
        self.gauges.append(gauge.Gauge(130, 40, 50, 250, 100, gauge.Gague_Type.RIGHT, self._display_surf))
        self.gauges.append(gauge.Gauge(130, 120, 50, 250, 100, gauge.Gague_Type.LEFT, self._display_surf))
        self.gauges.append(gauge.Gauge(400, 40, 250, 250, 100, gauge.Gague_Type.RADIAL, self._display_surf))

    def on_loop(self, update_time):
        """ Update loop """
        self.now += update_time
                
        for gauge in self.gauges:
            gauge.on_loop(update_time)

    def on_render(self):
        """ Render event """
        self._display_surf.fill((255, 0, 255))
        
        for gauge in self.gauges:
            gauge.on_render()

        pygame.display.update()

    def key_press(self, event):
        """ user input test """
        #if key == pygame.K_SPACE:
            