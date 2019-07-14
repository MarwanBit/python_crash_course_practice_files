import pygame
import sys 

class Bullet(pygame.sprite.Sprite):
	'''Creates the bullet class'''
	def __init__(self, screen, ship):
		'''Create a bullet object at the ship's current position'''
		super().__init__()
		self.screen = screen


		#Create a bullet rect at (0,0) and then set correct position
		self.rect = pygame.Rect(0,0, 15, 5)
		self.rect.centerx = ship.image_rect.centerx
		self.rect.top = ship.image_rect.top

		#Store the bullet's position as a decimal value
		self.y = float(self.rect.y)

		self.color = (190,190,190)
		self.speed_factor = 1

	def update(self):
		'''Move the bullet up the screen.'''
		#Update the decimal position of the bullet
		self.y -= self.speed_factor
		#Update the rect position
		self.rect.y = self.y

	def draw_bullet(self):
		'''Draw the bullet to the screen'''
		pygame.draw.rect(self.screen, self.color, self.rect)


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
				bullet.shot_loop_bool = True
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