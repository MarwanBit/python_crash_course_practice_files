import pygame
import sys
import random

class Star(pygame.sprite.Sprite):
	def __init__(self,screen):
		super().__init__()
		self.screen = screen
		self.image = pygame.image.load('star.bmp')
		self.image_rect = self.image.get_rect()
		self.centerx = self.image_rect.centerx 
		self.recty = self.image_rect.y
	def update(self):
		self.screen.blit(self.image,self.image_rect)

pygame.init()
width, height = 680, 420
loop_bool = True 
color = (230,230,230)
number_of_rows = 7 

screen = pygame.display.set_mode((width,height)) 

star_group = pygame.sprite.Group() 

for l in range(0,number_of_rows):
	for i in range(0,int(int(width))):
		if i % 100 == 0:
			stars = Star(screen)
			stars.centerx = random.randint(-10,10) + int(i)
			stars.image_rect.x = random.randint(-10,10) + int(i)
			stars.image_rect.y = random.randint(-10,10) + int(50*l)
			star_group.add(stars)
		

while loop_bool:

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

	screen.fill(color)

	for star in star_group:
		star.update()

	pygame.display.flip()