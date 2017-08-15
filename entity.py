from bullet import Bullet
from vector import Vector

import math
import random


class Entity:

	def __init__(self, start_position: Vector, health: int, color):
		self.color = color
		self.position = start_position
		self.health = health

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
		self.bullets.append(Bullet(position))

	def level_up(self):
		self.power += 10


class Enemy(Entity):

	def __init__(self, start_position: Vector, power: int, movement:str = "rand"):
		self.movement = movement
		self.power = power
		self.width = 15
		self.height = 15
		super(self.__class__, self).__init__(
			Vector(
				random.randrange(0 + self.width, 480 - self.width), 
				random.randrange(0 + self.height, 600 - self.height)
			), 100 * self.power, (255, 0, 0)
		)
		self.delta_vector = Vector(int(math.cos(math.radians(self.position.x)) * 10) // 2,
								 int(math.sin(math.radians(self.position.y)) * 10) // 2)
		

	def update_position(self):
		self.position.add(self.delta_vector)

