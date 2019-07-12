import pygame
	
width = 300
height = 400


if __name__ == "__main__":
	'''Runs the code below if the file is being executed directly'''
	pygame.init()
	screen = pygame.display.set_mode((width, height))
	loop_bool = True

	while loop_bool:
		'''Mainloop'''

		#updates the color of the screen
		screen.fill((0,0,255))

		#Event loop which catches the events
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				loop_bool = False

		#Updates the Screen
		pygame.display.flip()