import pygame
import random

class overlay:
	def __init__(self, width, height):
                random.seed()
                self.pickNewColour()
                self.colour = (self.red, self.green, self.blue)
		self.pos = (random.randrange(0,width), random.randrange(0,height))
		self.targetPos = (random.randrange(0,width), random.randrange(0,height))
		self.startPos = self.pos
		self.moveTime = 5
		self.startTime = 0;
		self.width = width
		self.height = height

	def draw(self, surface):
		pygame.draw.line(surface, self.colour, (0, self.pos[1]), (self.width, self.pos[1]))
		pygame.draw.line(surface, self.colour, (self.pos[0], 0), (self.pos[0], self.height))
		pygame.draw.circle(surface, self.colour, self.pos, 20, 1)
		pygame.draw.line(surface, self.colour, (self.pos[0] - 10, self.pos[1] - 10), (self.pos[0] - 18, self.pos[1] - 18))
		pygame.draw.line(surface, self.colour, (self.pos[0] + 10, self.pos[1] - 10), (self.pos[0] + 18, self.pos[1] - 18))
		pygame.draw.line(surface, self.colour, (self.pos[0] + 10, self.pos[1] + 10), (self.pos[0] + 18, self.pos[1] + 18))
		pygame.draw.line(surface, self.colour, (self.pos[0] - 10, self.pos[1] + 10), (self.pos[0] - 18, self.pos[1] + 18))
		
	def pickNewColour(self):
		self.red = random.randrange(10,255)
		self.green = random.randrange(10,255)
		self.blue = random.randrange(10,255)

		if self.red + self.green + self.blue < 255:
			selector = random.randrange(0,2)
			if selector == 0:
				self.red = random.randrange(200,255)
			if selector == 1:
				self.green = random.randrange(200,255)
			if selector == 2:
				self.blue = random.randrange(200,255)

	def update(self, updateTime):
		if self.pos == self.targetPos:
                        self.targetReached(updateTime)
		else:
			if updateTime > self.startTime + self.moveTime:
				self.targetReached(updateTime)
			else:
				timeOffset = (updateTime - self.startTime) / self.moveTime
				xPos = self.startPos[0] + ((self.targetPos[0] - self.startPos[0]) * timeOffset)
				yPos = self.startPos[1] + ((self.targetPos[1] - self.startPos[1]) * timeOffset)
				self.colour = (self.tweenColours(self.colour[0], self.red, timeOffset),self.tweenColours(self.colour[1], self.green, timeOffset),self.tweenColours(self.colour[2], self.blue, timeOffset))
				self.pos = (int(round(xPos)), int(round(yPos)))

	def targetReached(self, updateTime):
		self.pos = self.targetPos
		self.startPos = self.targetPos
		self.targetPos = (random.randrange(0, self.width), random.randrange(0, self.height))
		self.startTime = updateTime
		self.colour = (self.red, self.green, self.blue)
		self.pickNewColour()

	def tweenColours(self, startColour, endColour, progress):
		return (startColour - ((startColour - endColour) * progress)
