class Vector:

	def __init__(self, x, y):
		self.x = x
		self.y = y

	def add(self, v2):
		self.x += v2.x
		self.y += v2.y

