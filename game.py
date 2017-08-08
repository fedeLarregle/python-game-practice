import pygame, sys
from bullet import Bullet
from collision import *
from player import Player

from pygame.locals import *
from vector import Vector

class Game:

	SURFACE_WIDTH = 480
	SURFACE_HEIGHT = 600
	BACKGROUND_COLOR = (0, 0, 0)

	def __init__(self, player):
		pygame.init()
		self.game_font = pygame.font.SysFont("monospace", 15)
		self.enemies = [Enemy(Vector(480 // 2, 50)) for x in range(5)]
		self.player = player
		self.key_z = False
		self.key_up = False
		self.key_down = False
		self.key_left = False
		self.key_right = False


	def run(self):
		done = False
		main_surface = pygame.display.set_mode((self.SURFACE_WIDTH, self.SURFACE_HEIGHT))
		clock = pygame.time.Clock()

		while not done:

			for event in pygame.event.get():
				# I know... we need to do something else than 'sys.exit()' when the player's health goes down to 0...
				if event.type == pygame.QUIT or self.player.health <= 0:
					pygame.quit()
					sys.exit()

				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_DOWN:
						self.key_down = True
					if event.key == pygame.K_UP:
						self.key_up = True
					if event.key == pygame.K_RIGHT:
						self.key_right = True
					if event.key == pygame.K_LEFT:
						self.key_left = True
					if event.key == pygame.K_z:
						self.key_z = True
				elif event.type == pygame.KEYUP:
					if event.key == pygame.K_DOWN:
						self.key_down = False
					if event.key == pygame.K_UP:
						self.key_up = False
					if event.key == pygame.K_LEFT:
						self.key_left = False
					if event.key == pygame.K_RIGHT:
						self.key_right = False
					if event.key == pygame.K_z:
						self.key_z = False

			for enemy in self.enemies:
				# Checking if our enemy is colliding with any wall
				# in that case we invert the direction of our enemy
				if Collisions.check_left_wall(enemy):
					enemy.delta_vector.x = -enemy.delta_vector.x

				if  Collisions.check_right_wall(enemy, self.SURFACE_WIDTH):
					enemy.delta_vector.x = -enemy.delta_vector.x

				if Collisions.check_bottom_wall(enemy, self.SURFACE_HEIGHT):
					enemy.delta_vector.y = -enemy.delta_vector.y

				if Collisions.check_top_wall(enemy):
					enemy.delta_vector.y = -enemy.delta_vector.y
				# Checking the our player and enemy are colliding
				if Collisions.check_player_enemy_collision(self.player, enemy):
					self.player.health -= 1

			# Checking if our player is trying to go out of the window
			# in that case we don't allow it...
			if self.key_up:
				if not Collisions.check_top_wall(self.player):
					self.player.move_up()
			if self.key_down:
				if not Collisions.check_bottom_wall(self.player, self.SURFACE_HEIGHT):
					self.player.move_down()
			if self.key_right:
				if not Collisions.check_right_wall(self.player, self.SURFACE_WIDTH):
					self.player.move_right()
			if self.key_left:
				if not Collisions.check_left_wall(self.player):
					self.player.move_left()
			if self.key_z:
				self.player.add_bullet()
				self.key_z = False

			main_surface.fill(self.BACKGROUND_COLOR)
			pygame.draw.circle(main_surface, self.player.color, (self.player.position.x, self.player.position.y), self.player.width)
			for enemy in self.enemies:
				pygame.draw.circle(main_surface, enemy.color, (enemy.position.x, enemy.position.y), enemy.width)
				enemy.update_position()

			for b in self.player.bullets:
				b.shoot()
				pygame.draw.circle(main_surface, b.color, (b.position.x, b.position.y), b.width)

			# remove bullets that have gone away
			self.player.bullets = [b for b in self.player.bullets if not Collisions.check_top_wall(b)]

			# remove all the bullets that have hit an enemy
			# and if it has hit an enemy, reduce that enemy's life
			i = 0
			while i < len(self.player.bullets):
				for e in self.enemies:
					if i < len(self.player.bullets) and Collisions.check_circle_circle_collision(self.player.bullets[i], e):
						del self.player.bullets[i]
						e.health -= 10
						self.player.points += 10
				i += 1
			# remove all the enemies that have a health less or equal to 0
			self.enemies = [e for e in self.enemies if not e.health <= 0]
			# player health to be render onto the main_surface
			health_info = self.game_font.render(''.join(["Player health: ", str(self.player.health)]), 1, (255, 255, 255))
			main_surface.blit(health_info, (self.SURFACE_WIDTH // 10, self.SURFACE_HEIGHT // 14))
			# player points to be render onto the main_surface
			points_info = self.game_font.render(''.join(["Player points: ", str(self.player.points)]), 1, (255, 255, 255))
			main_surface.blit(points_info, ((self.SURFACE_WIDTH // 2) + self.SURFACE_WIDTH // 7, self.SURFACE_HEIGHT // 14))
			pygame.display.flip()
			clock.tick(30)

player = Player(Vector(480 // 2, 600 // 2))
game = Game(player)
game.run()

