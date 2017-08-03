from enemy import Enemy
from entity import Entity
from player import Player

class Collisions:

	@staticmethod
	def check_right_wall(entity: Entity, SURFACE_WIDTH: int):
		if (entity.position.x + entity.width) >= SURFACE_WIDTH:
			return True

	@staticmethod
	def check_left_wall(entity: Entity):
		if (entity.position.x - entity.width) <= 0:
			return True

	@staticmethod
	def check_top_wall(entity: Entity):
		if (entity.position.y - entity.height) <= 0:
			return True

	@staticmethod
	def check_bottom_wall(entity: Entity, SURFACE_HEIGHT: int):
		if (entity.position.y + entity.height) >= SURFACE_HEIGHT:
			return True

	@staticmethod
	def check_player_enemy_collision(player: Player, enemy: Enemy):
		x_dif = player.position.x - enemy.position.x
		y_dif = player.position.y - enemy.position.y
		square_distance = (x_dif * x_dif) + (y_dif * y_dif)
		
		return (square_distance <= ( (player.width + enemy.width) * (player.width + enemy.width) ))
