from bullet import Bullet
from entity import Entity
from vector import Vector

class Player(Entity):

	def __init__(self, start_position: Vector, power:int = 10):
		super(self.__class__, self).__init__(start_position, 100, (255, 255, 255))
		self.power = power
		self.bullets = []
		self.points = 0
		self.width = 20
		self.height = 20

	def move_down(self):
		v2 = Vector(0, 4)
		self.position.add(v2)

	def move_up(self):
		v2 = Vector(0, -4)
		self.position.add(v2)

	def move_right(self):
		v2 = Vector(4, 0)
		self.position.add(v2)

	def move_left(self):
		v2 = Vector(-4, 0)
		self.position.add(v2)

	def add_bullet(self, position:Vector):
		self.bullets.append(Bullet(self, position))

	def level_up(self):
		self.power += 10

