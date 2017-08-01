from vector import Vector

class Player:

	def __init__(self, start_position):
		self.position = start_position
		self.color = (255, 255, 255)

	def move_down(self):
		v2 = Vector(0, 5)
		self.position.add(v2)

	def move_up(self):
		v2 = Vector(0, -5)
		self.position.add(v2)

	def move_right(self):
		v2 = Vector(5, 0)
		self.position.add(v2)

	def move_left(self):
		v2 = Vector(-5, 0)
		self.position.add(v2)

