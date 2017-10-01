import random

class blip:
	def __init__(self, width, height):
		self.width = width
		self.height = height

		self.now = 0
		self.startTime = 0
		self.moveTime = random.randrange(50, 75)
		self.pos = (random.randrange(0,width), random.randrange(0,height))
		self.startPos = self.pos
		self.targetPos = (random.randrange(0,width), random.randrange(0,height))

		self.strength = 50

	def on_loop(self, updateTime):
		self.now += updateTime

		if self.pos == self.targetPos:
			self.targetReached(self.now)
		else:
			if self.now > self.startTime + self.moveTime:
				self.targetReached(self.now)
			else:
				timeOffset = (self.now - self.startTime) / self.moveTime
				xPos = self.startPos[0] + ((self.targetPos[0] - self.startPos[0]) * timeOffset)
				yPos = self.startPos[1] + ((self.targetPos[1] - self.startPos[1]) * timeOffset)
				self.pos = (int(round(xPos)), int(round(yPos)))

	def targetReached(self, updateTime):
		self.now = 0
		self.pos = self.targetPos
		self.startPos = self.targetPos
		self.targetPos = (random.randrange(0, self.width), random.randrange(0, self.height))
		self.moveTime = random.randrange(50, 75)