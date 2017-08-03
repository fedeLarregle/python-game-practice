from vector import Vector

class Entity:

	def __init__(self, start_position: Vector, health: int, color):
		self.color = color
		self.position = start_position
		self.health = health
