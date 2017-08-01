import pygame, sys
from pygame.locals import *
from player import Player
from vector import Vector

class Game:

	SURFACE_WIDTH = 480
	SURFACE_HEIGHT = 480
	BACKGROUND_COLOR = (0, 0, 0)

	def __init__(self, player):
		pygame.init()
		self.player = player
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
				if event.type == pygame.QUIT:
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
				elif event.type == pygame.KEYUP:
					if event.key == pygame.K_DOWN:
						self.key_down = False
					if event.key == pygame.K_UP:
						self.key_up = False
					if event.key == pygame.K_LEFT:
						self.key_left = False
					if event.key == pygame.K_RIGHT:
						self.key_right = False

			if self.key_up:
				self.player.move_up()
			if self.key_down:
				self.player.move_down()
			if self.key_right:
				self.player.move_right()
			if self.key_left:
				self.player.move_left()

			main_surface.fill(self.BACKGROUND_COLOR)
			pygame.draw.rect(main_surface, self.player.color, (self.player.position.x, self.player.position.y, 25, 25))
			pygame.display.flip()
			
			clock.tick(30)

start_position = Vector(480 // 2, 480 // 2)
player = Player(start_position)
game = Game(player)
game.run()

