import pygame 
import sys
import random

class RocketGameSettings():
	'''create the settings for this mini-game'''
	def __init__(self,height,width):
		'''initializes the settings class'''
		self.height = height
		self.width = width
		self.acceleration_constant = 1.5 

class Star(pygame.sprite.Sprite):
	'''class which creates a star'''

	def __init__(self, screen, settings):
		'''intializes the star'''
		super().__init__()
		#Store the screen and settings in the instance of the object
		self.screen = screen 
		self.settings = settings 

		#Stores the object of the star
		self.image = pygame.image.load('star.bmp')
		self.image_rect =self.image.get_rect() #get the rectangular coords of the star 

		#rectangle properties
		self.image_rect.centerx = self.image_rect.centerx
		self.image_rect.bottom = self.image_rect.bottom 
		self.image_rect.centery = self.image_rect.centery

		#rectangle properties of the screen
		self.screen_rect = self.screen.get_rect()
		self.screen_rect_centerx = self.screen_rect.centerx 
		self.screen_rect_bottom = self.screen_rect.bottom

	def draw_sprite(self,screen):
		'''draws the sprite'''
		self.screen.blit(self.image, self.image_rect)

class Rocket(pygame.sprite.Sprite):
	'''class which handles the rocket object''' 
	def __init__(self, screen, settings):
		'''initializes the rocket class'''
		#Initializes the parent class
		super().__init__()
		#loads the image of the rocket sprite 
		self.image = pygame.image.load('rocket.bmp')
		self.image_rect = self.image.get_rect() #gets the rectangle coordinates of the sprite
		#Gets the pygame screen and stores it in the object 
		self.screen = screen
		self.screen_rect = self.screen.get_rect() #Gets the rectangular coordinates of the screen
		self.image_rect.centerx = self.screen_rect.centerx #centers x in relation to the screen
		self.image_rect.bottom = self.screen_rect.bottom #sets the bottom y coord to the scren coord

		#Gets the settings input
		self.settings = settings

		#Below are movement flags used to manage the movement of the rocket sprite
		self.right_movement_flag = False
		self.left_movement_flag = False 
		self.up_movement_flag = False
		self.down_movement_flag = False
		self.acceleration_constant = self.settings.acceleration_constant #sets the movement acceleration constant

	def draw_rocket(self,screen):
		'''draws the rocket on the screen''' 
		#Draws the rocket over the screen project
		self.screen.blit(self.image, self.image_rect)

	def update(self): 
		'''updates the position of the rocket depending on what key you are pressing'''
		if self.right_movement_flag and self.image_rect.right < self.screen_rect.right:
			self.image_rect.centerx += self.acceleration_constant 
		if self.left_movement_flag and self.image_rect.left > self.screen_rect.left: 
			self.image_rect.centerx -= self.acceleration_constant
		if self.up_movement_flag and self.image_rect.top > self.screen_rect.top:
			self.image_rect.centery -= self.acceleration_constant
		if self.down_movement_flag and self.image_rect.bottom < self.screen_rect.bottom:
			self.image_rect.centery += self.acceleration_constant


if __name__ == "__main__":
	'''runs the game if not being imported'''
	#initalizes the pygame modules
	pygame.init()
	stg = RocketGameSettings(500,500)
	screen = pygame.display.set_mode((stg.height,stg.width))
	pygame.display.set_caption('Rocket Game')
	loop_bool = True
	rocket = Rocket(screen,stg)

	#Creates a group of stars
	stars = pygame.sprite.Group()
	for i in range(0,20):
		star = Star(screen,stg)
		star.image_rect.centerx = random.randint(-20,500)
		star.image_rect.centery = random.randint(-20,500)
		stars.add(star)

	print(stars)	

	while loop_bool:
		'''game's mainloop''' 

		#fills the screen with white 
		screen.fill((0,0,0))

		#event loop
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit() 
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					rocket.left_movement_flag = True
				if event.key == pygame.K_RIGHT:
					rocket.right_movement_flag = True
				if event.key == pygame.K_UP:
					rocket.up_movement_flag = True
				if event.key == pygame.K_DOWN:
					rocket.down_movement_flag = True
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_LEFT:
					rocket.left_movement_flag = False
				if event.key == pygame.K_RIGHT:
					rocket.right_movement_flag = False 
				if event.key == pygame.K_UP:
					rocket.up_movement_flag = False 
				if event.key == pygame.K_DOWN:
					rocket.down_movement_flag = False

		#Updates the rocket's position
		rocket.update()

		#draws the stars
		for star in stars:
			star.draw_sprite(screen)

		#draws the rocket on top 
		rocket.draw_rocket(screen) 

		#updates the screen 
		pygame.display.flip()