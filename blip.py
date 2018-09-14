"""Blips for displaying on a radar"""

import random

class Blip:
    """A blip to move on a display"""
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.now = 0
        self.start_time = 0
        self.moveTime = random.randrange(50, 75)
        self.pos = (random.randrange(0,width), random.randrange(0,height))
        self.startPos = self.pos
        self.targetPos = (random.randrange(0,width), random.randrange(0,height))

        self.strength = 50

    def on_loop(self, updateTime):
        self.now += updateTime

        if self.pos == self.targetPos:
            self.target_reached()
        else:
            if self.now > self.start_time + self.moveTime:
                self.target_reached()
            else:
                time_offset = (self.now - self.start_time) / self.moveTime
                x_pos = self.startPos[0] + ((self.targetPos[0] - self.startPos[0]) * time_offset)
                y_pos = self.startPos[1] + ((self.targetPos[1] - self.startPos[1]) * time_offset)
                self.pos = (int(round(x_pos)), int(round(y_pos)))

    def target_reached(self):
        """Blip has reached the target positions"""
        self.now = 0
        self.pos = self.targetPos
        self.startPos = self.targetPos
        self.targetPos = (random.randrange(0, self.width), random.randrange(0, self.height))
        self.moveTime = random.randrange(50, 75)
