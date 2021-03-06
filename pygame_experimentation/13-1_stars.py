import pygame
import sys

Width, Height = 680, 420
loop_bool = True

screen = pygame.display.set_mode((Width,Height))

class Star(pygame.sprite.Sprite):
	def __init__(self,screen):
		super().__init__()
		self.screen = screen 
		self.image = pygame.image.load('star.bmp')
		self.image_rect = self.image.get_rect()
		self.centerx = self.image_rect.centerx
	def update(self):
		self.screen.blit(self.image,self.image_rect)

star = Star(screen)
star_group = pygame.sprite.Group()
number_of_rows = 7

for l in range(0,number_of_rows):
	for i in range(0,int(int(Width))):
		if i % 100 == 0:
			stars = Star(screen)
			stars.centerx = int(i)
			stars.image_rect.x = int(i)
			stars.image_rect.y = int(50*l)
			star_group.add(stars)


while loop_bool:

	screen.fill((230,230,230))
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
	star_group.update()

	pygame.display.flip()