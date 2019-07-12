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
		self.acceleration_constant = 1
		self.image_rect.centerx = self.screen_rect.centerx
		self.image_rect.bottom = self.screen_rect.bottom

	def draw_sprite(self):
		'''Draws the sprite ontop of the screen'''
		self.image_rect.centerx = self.image_rect.centerx 
		self.image_rect.bottom = self.image_rect.bottom 
		self.screen.blit(self.image, self.image_rect)


#Runs the file if it's ran directly
if __name__ == "__main__":

	#Initial settings
	height = 600
	width = 600
	pygame.init()

	#Intializes the screen
	screen = pygame.display.set_mode((width, height))
	pygame.display.set_caption('Test Pokemon')
	loop_bool = True

	#creates the gallade image sprite
	sprite = Gallade(screen)

	while loop_bool:
		'''Mainloop'''

		#Fills the screen with a white color
		screen.fill((255,255,255))

		for event in pygame.event.get():
			'''Event loop'''
			if event.type == pygame.QUIT:
				'''Exits the loop if we press the quit button'''
				sys.exit()
			if event.type == pygame.KEYDOWN:
				'''Executes certain events depending on which key is pressed'''
				#controls an event when the left key is pressed
				if event.key == pygame.K_LEFT:
					sprite.image_rect.centerx = sprite.image_rect.centerx - sprite.acceleration_constant
				if event.key == pygame.K_RIGHT:
					sprite.image_rect.centerx = sprite.image_rect.centerx + sprite.acceleration_constant

		#Draw the Gallade Image
		sprite.draw_sprite()


		#Updates the screen
		pygame.display.flip()
