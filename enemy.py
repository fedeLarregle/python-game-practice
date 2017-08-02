from vector import Vector

class Enemy:

	def __init__(self, start_position: Vector):
		self.position = start_position
		self.width = 20
		self.height = 20
		self.health = 50
		self.color = (255, 0, 0)
