#!/usr/bin/env python
'''

For this exercise, draw a circle wherever the user clicks the mouse

'''
import sys, pygame, random
from datetime import date
assert sys.version_info >= (3,4), 'This script requires at least Python 3.4' 

screen_size = (800,600)
FPS = 60
black = (0,0,0)
white = (255,255,255)

def main():
	pygame.init()
	screen = pygame.display.set_mode(screen_size)
	font = pygame.font.SysFont("arial",64)
	clock = pygame.time.Clock()


	while True:
		clock.tick(FPS)
		screen.fill(black)
		colors = ((0,0,0),(255,255,255),(255,0,0))
		x = random.randint(0, 800)
		y = random.randint(0, 600)
		radius = random.randrange(100)
		color = colors[random.randrange(len(colors))]
		pygame.draw.circle(screen, colors, (x, y), radius)


		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit(0)
			if event.type == pygame.MOUSEBUTTONUP:
				pos = pygame.mouse.get_pos()



		pygame.display.flip()

if __name__ == '__main__':
	main()