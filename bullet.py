from entity import Entity
from vector import Vector

class Bullet:

	def __init__(self, entity: Entity, position:Vector):
		self.entity = entity
		self.position = position
		self.color = (255, 255, 0)
		self.width = 8
		self.height = 8

	def shoot(self):
		self.position.add(Vector(0, -6))

