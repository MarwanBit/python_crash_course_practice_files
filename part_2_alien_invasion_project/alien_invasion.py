''' 
The required modules below are sys and pygame, each
can be installed using pip install <name of module>
ex: pip install sys
'''

import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from alien import Alien

def run_game():
	#Initialize the game and creates a screen object
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode(
		(ai_settings.screen_width, ai_settings.screen_height))
	pygame.display.set_caption("Alien Invasion")

	#Make a ship, a group of bullets, and a group of aliens.
	space_ship = Ship(ai_settings, screen)
	#Make a group to store bullets in.
	bullets = Group()
	aliens = Group()

	#Create the fleet of aliens.
	gf.create_fleet(ai_settings, screen, space_ship, aliens)

	#Set the background color
	bg_color = (230,230,20)


	#Make an alien.
	alien = Alien(ai_settings, screen)

	#Start the main loop for the game
	while True:

		#Watch for keyboard and mouse events
		gf.check_events(ai_settings, screen, space_ship, bullets)
		space_ship.update()
		bullets.update()
		#Get rid of bullets that have dissappeared
		gf.update_bullets(bullets)
		#updates the screen 
		gf.update_screen(ai_settings, screen, space_ship, aliens, bullets)


run_game()