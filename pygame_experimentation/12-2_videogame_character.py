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

		#movement flags
		self.moving_right_flag = False
		self.moving_left_flag = False
		#Speed Factor/ Speed controls
		self.ship_speed_factor = 1.5

	def draw_sprite(self):
		'''Draws the sprite ontop of the screen'''
		self.image_rect.centerx = self.image_rect.centerx 
		self.image_rect.bottom = self.image_rect.bottom 
		self.screen.blit(self.image, self.image_rect)

	def update(self):
		'''updates the movement flag depending on which key is pressed'''
		if self.moving_right_flag and self.image_rect.right < self.screen_rect.right:
			self.image_rect.centerx += 1
		if self.moving_left_flag and self.image_rect.left > self.screen_rect.left:
			self.image_rect.centerx -= 1
			


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
					sprite.moving_left_flag = True					
				if event.key == pygame.K_RIGHT:
					sprite.moving_right_flag = True					
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_LEFT:
					sprite.moving_left_flag = False
				if event.key == pygame.K_RIGHT:
					sprite.moving_right_flag = False 
	
		#update's the sprite
		sprite.update()

		#Draw the Gallade Image
		sprite.draw_sprite()

		#Updates the screen
		pygame.display.flip()
