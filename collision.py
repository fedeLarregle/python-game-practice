
class Collisions:

	@staticmethod
	def check_right_wall(player, SURFACE_WIDTH):
		if (player.position.x + player.width) == SURFACE_WIDTH:
			return True

	@staticmethod
	def check_left_wall(player):
		if (player.position.x - player.width) == 0:
			return True

	@staticmethod
	def check_top_wall(player):
		if (player.position.y - player.height) == 0:
			return True

	@staticmethod
	def check_bottom_wall(player, SURFACE_HEIGHT):
		if (player.position.y + player.height) == SURFACE_HEIGHT:
			return True
