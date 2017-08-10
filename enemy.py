from entity import Entity
from vector import Vector

import math
import random

class Enemy(Entity):

	def __init__(self, start_position: Vector, power: int):
		self.power = power
		self.width = 15
		self.height = 15
		super(self.__class__, self).__init__(
			Vector(
				random.randrange(0 + self.width // 2, 480 - self.width // 2), 
				random.randrange(0 + self.height, 600 - self.height // 2)
			), 50 * self.power, (255, 0, 0)
		)
		self.delta_vector = Vector(int(math.cos(math.radians(self.position.x)) * 10) // 2,
								 int(math.sin(math.radians(self.position.y)) * 10) // 2)
		

	def update_position(self):
		self.position.add(self.delta_vector)


