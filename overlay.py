import pygame
import random

class overlay:
	def __init__(self):
		self.colour = (0, 255, 0)
		self.pos = (50, 50)
		self.targetPos = (50, 50)
		self.startPos = (50, 50)
		self.moveTime = 5
		self.startTime = 0;
		random.seed(3)

	def draw(self, surface, width, height):
		pygame.draw.line(surface, self.colour, (0, self.pos[1]), (width, self.pos[1]))
		pygame.draw.line(surface, self.colour, (self.pos[0], 0), (self.pos[0], height))
		pygame.draw.circle(surface, self.colour, self.pos, 20, 1)
		pygame.draw.line(surface, self.colour, (self.pos[0] - 10, self.pos[1] - 10), (self.pos[0] - 18, self.pos[1] - 18))
		pygame.draw.line(surface, self.colour, (self.pos[0] + 10, self.pos[1] - 10), (self.pos[0] + 18, self.pos[1] - 18))
		pygame.draw.line(surface, self.colour, (self.pos[0] + 10, self.pos[1] + 10), (self.pos[0] + 18, self.pos[1] + 18))
		pygame.draw.line(surface, self.colour, (self.pos[0] - 10, self.pos[1] + 10), (self.pos[0] - 18, self.pos[1] + 18))
		pass

	def update(self, updateTime, width, height):
		if self.pos == self.targetPos:
			self.startPos = self.targetPos
			self.targetPos = (random.randrange(0, width), random.randrange(0, height))
			self.startTime = updateTime
		else:
			if updateTime > self.startTime + self.moveTime:
				self.targetReached()
			else:
				timeOffset = (updateTime - self.startTime) / self.moveTime
				xPos = self.startPos[0] + ((self.targetPos[0] - self.startPos[0]) * timeOffset)
				yPos = self.startPos[1] + ((self.targetPos[1] - self.startPos[1]) * timeOffset)
				self.pos = (int(round(xPos)), int(round(yPos)))
		
		pass

	def targetReached(self):
		self.pos = self.targetPos
		pass
