import pygame
import sys 

class Bullet(pygame.sprite.Sprite):
	'''Creates the bullet class'''
	def __init__(self,screen,ship):
		#defines the ship and height of a bullet
		self.width = 3
		self.height = 15 
		#gives you access to  the ship and screen
		self.screen = screen 
		self.screen_rect = self.screen.get_rect()
		self.ship = ship.screen_rect.bottom

		#creates the bullet rectangle object
		self.bullet_image = pygame.Rect(0,0,self.width, self.height)
		self.bullet_color = (230,230,230)
		self.bullet_image_top = self.bullet_image.top
		#sets the top of the bullet to be equal to the top of the ship
		self.bullet_image_top = self.ship
		#Speed of the Bullet
		self.speed_factor = 1 

	def draw_bullet(self):
		'''draws the bullet'''
		pygame.draw.rect(self.screen, self.bullet_color, self.bullet_image)

	def bullet_update(self):
		'''updates the bullet when space bar is pressed'''
		self.bullet_image.x -= self.speed_factor


class Ship(pygame.sprite.Sprite):
	'''creates the ship class/ object'''
	def __init__(self,screen):
		'''intializes the ship object'''
		super().__init__() #intializes the parent class 
		
		#creates and imports the image of the ship
		self.image = pygame.image.load('space_ship.bmp') #gets the picture
		self.image_rect = self.image.get_rect() #gets the rectangular coords of the pic

		#saves the screen which is being used
		self.screen = screen 
		self.screen_rect = self.screen.get_rect()
		self.screen_rect_centery = self.screen_rect.centery 

		#sets the coords of the ship 
		self.image_rect.centery = self.screen_rect_centery

		#Movement Flags
		self.right_movement_flag = False
		self.left_movement_flag = False

		#Acceleration constant
		self.acceleration_constant = 1.5

	def draw_sprite(self):
		'''draws the sprite over the screen'''
		self.image = pygame.transform.scale(self.image, (100, 130))
		self.screen.blit(pygame.transform.rotate(self.image, 90), self.image_rect)

	def update_sprite(self):
		'''update's the sprites position'''
		if self.right_movement_flag and self.image_rect.top > self.screen_rect.top: 
			self.image_rect.centery -= self.acceleration_constant
		if self.left_movement_flag and self.image_rect.bottom < self.screen_rect.bottom:
			self.image_rect.centery += self.acceleration_constant


#initializes the pygame modules
pygame.init()
#loop flag used for the mainloop of the program
loop_bool = True
#Initializes the screen
width_and_height_tuple = (500,600)
screen = pygame.display.set_mode(width_and_height_tuple)
pygame.display.set_caption("Sideways Shooter")

#Creates the ship
ship = Ship(screen)
#Flip the ship

bullet = Bullet(screen, ship)
bullets = pygame.sprite.Group()

while loop_bool:
	'''the mainloop which refreshes the screen with each change'''

	#fills the screen with the color white 
	screen.fill((255,255,255))

	#The main event loop
	for event in pygame.event.get():
		#Checks for someone clicking the red exit button
		if event.type == pygame.QUIT:
			#quits the application
			sys.exit()
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_RIGHT:
				ship.right_movement_flag = True
			if event.key == pygame.K_LEFT:
				ship.left_movement_flag = True
			if event.key == pygame.K_SPACE:
				bullet.bullet_update()
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_RIGHT:
				ship.right_movement_flag = False
			if event.key == pygame.K_LEFT:
				ship.left_movement_flag = False

	#Updates the ship's position
	ship.update_sprite()


	#draw the bullets
	bullet.draw_bullet()

	#draw the ship
	ship.draw_sprite()


	#updates the screen 
	pygame.display.flip()