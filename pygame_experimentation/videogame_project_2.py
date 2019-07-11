import pygame

class Screen(pygame.Surface):

	def __init__(self):
		'''Initializes the screen with a size of 400, 600'''
		self.width = 600
		self.height = 400
		#Initializes the parent class Surface object
		super().__init__(size =(self.width,self.height))

		


if __name__ == "__main__":
	'''Runs the code below if the file is being executed directly'''
	pygame.init()
	window = Screen()
	print(window)
	pygame.display.set_mode(self.width, self.height)