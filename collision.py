from enemy import Enemy
from player import Player

class Collisions:

	@staticmethod
	def check_right_wall(player: Player, SURFACE_WIDTH: int):
		if (player.position.x + player.width) == SURFACE_WIDTH:
			return True

	@staticmethod
	def check_left_wall(player: Player):
		if (player.position.x - player.width) == 0:
			return True

	@staticmethod
	def check_top_wall(player: Player):
		if (player.position.y - player.height) == 0:
			return True

	@staticmethod
	def check_bottom_wall(player: Player, SURFACE_HEIGHT: int):
		if (player.position.y + player.height) == SURFACE_HEIGHT:
			return True

	@staticmethod
	def check_player_enemy_collision(player: Player, enemy: Enemy):
		x_dif = player.position.x - enemy.position.x
		y_dif = player.position.y - enemy.position.y
		square_distance = (x_dif * x_dif) + (y_dif * y_dif)
		
		return (square_distance <= ( (player.width + enemy.width) * (player.width + enemy.width) ))
