import pygame
import sys

class Gallade(pygame.sprite.Sprite):
	'''Creates and editable sprite for the pokemon Gallade'''

	def __init__(self, screen):
		'''Initializes the Gallade Sprite'''
		#Super().__init__() intializes the pygame.sprite parent class
		super().__init__()
		self.screen = screen
		self.screen_rect = self.screen.get_rect()
		self.image = pygame.image.load('gallade.bmp')
		self.image_rect = self.image.get_rect()

	def draw_sprite(self):
		'''Draws the sprite ontop of the screen'''
		self.image_rect.centerx = self.screen_rect.centerx
		self.image_rect.bottom = self.screen_rect.bottom
		self.screen.blit(self.image, self.image_rect)


#Runs the file if it's ran directly
if __name__ == "__main__":

	#Initial settings
	height = 600
	width = 600
	pygame.init()

	#Intializes the screen
	screen = pygame.display.set_mode((width, height))
	loop_bool = True

	#creates the gallade image sprite
	sprite = Gallade(screen)

	while loop_bool:
		'''Mainloop'''

		#Fills the screen with a white color
		screen.fill((255,255,255))

		#Draw the Gallade Image
		sprite.draw_sprite()

		for event in pygame.event.get():
			'''Event loop'''
			if event.type == pygame.QUIT:
				'''Exits the loop if we press the quit button'''
				sys.exit()


		#Updates the screen
		pygame.display.flip()
