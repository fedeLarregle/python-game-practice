class Vector:

	def __init__(self, x: int, y: int):
		self.x = x
		self.y = y

	def add(self, v2):
		self.x += v2.x
		self.y += v2.y

