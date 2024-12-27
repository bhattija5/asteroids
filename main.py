# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame, constants
from constants import *

SCREEN_HEIGHT = constants.SCREEN_HEIGHT
SCREEN_WIDTH = constants.SCREEN_WIDTH

def main():
	pygame.init()
	print("Starting asteroids!")
	print(f"Screen width: {constants.SCREEN_WIDTH}")
	print(f"Screen height: {constants.SCREEN_HEIGHT}")
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	while True:
		for event in pygame.event.get():
    			if event.type == pygame.QUIT:
       				return
		screen.fill("black")
		pygame.display.flip()
if __name__ == "__main__":
    main()
