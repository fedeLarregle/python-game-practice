from entity import Entity
from vector import Vector

class Bullet:

	def __init__(self, entity: Entity):
		self.entity = entity
		self.position = Vector(self.entity.position.x, self.entity.position.y)
		self.color = (128, 128, 128)
		self.width = 10
		self.height = 10

	def shoot(self):
		self.position.add(Vector(0, -6))
