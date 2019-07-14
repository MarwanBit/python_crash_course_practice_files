import pygame
import sys

loop_bool = True

pygame.init()
screen = pygame.display.set_mode((300,300))

while loop_bool:

	for event in pygame.event.get():
		if event.type == pygame.KEYDOWN:
			print(event.key)
		if event.type == pygame.QUIT:
			sys.exit()

	pygame.display.flip()