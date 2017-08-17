from utils import TimeUtils

import math
import random

# TODO this is just a 'first' attempt of a level class so let's see what happens :P
class Level:

	def __init__(self):
		self.sprites = [Sprite(20, 16, random.randrange(0, 5)) for x in range(0, (20 * 16)) ]


class Sprite:

	def __init__(self, width:int, height:int, value:int = 0):
		self.width = width
		self.height = height
		self.value = value

