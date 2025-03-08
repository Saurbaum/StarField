"""Provides a scifi display for background visuals"""

import sys
import ctypes
import pygame
import starfield_scanner
import radar
import forward_sweep
import target
import control_display
import sea

class App:
    """Applicaiton for starfield scanner"""
    def __init__(self):
        self._running = True
        self._display_surf = None
        self.active_display = None
        self.clock = pygame.time.Clock()
        self.now = 0
        self.target_count = 50
        self.targets = []

        pygame.init()
        pygame.mouse.set_visible(False)

        if sys.platform.startswith("win32"):
            ctypes.windll.user32.SetProcessDPIAware()

        width, height = pygame.display.Info().current_w, pygame.display.Info().current_h
        self._display_surf = pygame.display.set_mode(
            (width, height), pygame.NOFRAME | pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._running = True

        for x in range(self.target_count):
            self.targets.append(target.Target(width, height))

        self.starfield_scanner = starfield_scanner.StarfieldScanner(
            width, height, self._display_surf)
        self.radar = radar.Radar(width, height, self._display_surf, self.targets)
        self.forward_sweep = forward_sweep.ForwardSweep(width, height, self._display_surf, self.targets, height/3, 0)
        self.control_display = control_display.ControlDisplay(width, height, self._display_surf)
        self.sea_display = sea.Sea(width, height, self._display_surf)
        self.active_display = self.starfield_scanner

    def on_event(self, event):
        """Event Handling"""
        if event.type == pygame.QUIT:
            self._running = False

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_ESCAPE:
                self._running = False
            elif event.key == pygame.K_1:
                self.active_display = self.starfield_scanner
            elif event.key == pygame.K_2:
                self.active_display = self.radar
            elif event.key == pygame.K_3:
                self.active_display = self.forward_sweep
            elif event.key == pygame.K_4:
                self.active_display = self.control_display
            elif event.key == pygame.K_5:
                self.active_display = self.sea_display

        self.active_display.key_press(event)

    def on_loop(self):
        """Main logic loop"""
        self.now = self.clock.get_rawtime() / 1000
        self.starfield_scanner.on_loop(self.now)
        self.radar.on_loop(self.now)
        self.forward_sweep.on_loop(self.now)
        self.control_display.on_loop(self.now)
        self.sea_display.on_loop(self.now)
        for target in self.targets:
            target.on_loop(self.now)

    def on_render(self):
        """Render loop"""
        self.active_display.on_render()
        pygame.display.update()

    def on_execute(self):
        """Setup applicaiton"""

        while self._running:
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
            self.clock.tick(60)

        pygame.quit()

if __name__ == "__main__":
    APP = App()
    APP.on_execute()
