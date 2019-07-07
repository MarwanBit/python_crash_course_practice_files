''' 
The required modules below are sys and pygame, each
can be installed using pip install <name of module>
ex: pip install sys
'''

import pygame
from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
	#Initialize the game and creates a scren object
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode(
		(ai_settings.screen_width, ai_settings.screen_height))
	pygame.display.set_caption("Alien Invasion")

	#Make a ship 
	space_ship = Ship(ai_settings, screen)

	#Set the background color
	bg_color = (230,230,20)

	#Start the main loop for the game
	while True:

		#Watch for keyboard and mouse events
		gf.check_events(space_ship)
		space_ship.update()
		#updates the screen 
		gf.update_screen(ai_settings, screen, space_ship)


run_game()