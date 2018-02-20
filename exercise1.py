#!/usr/bin/env python
'''

For every line, please add a comment describing what it does. 

Try to describe each line within the context of the program as a whole, rather than just mechanically

Feel free to alter the parameters to see how things change. That can be a great way to be able to intuit what is supposed to be happening

I will do the first two lines for you as an example


'''
import sys, pygame	# imports the sys and pygame modules so they can be used in this program
assert sys.version_info >= (3,4), 'This script requires at least Python 3.4' # requires that the Python 3.4 (or higher version) interpreter is being used; i.e., not compatible with Python 2

screen_size = (800,600) #Gives the window that will be shown it's width and length
FPS = 60 #How smooth things will run in the window

def main():
	pygame.init() #This is a way of implementing pygame .. Something that needs to be done before
	screen = pygame.display.set_mode(screen_size) #This is defining the screen(window) that will appear
	clock = pygame.time.Clock()

	while True:
		clock.tick(FPS) #This is calculating user to pc input
		screen.fill((0,0,0)) #Fills the screen with whatever color is coded .. In this case, black

		for event in pygame.event.get():
			if event.type == pygame.QUIT: #Something that needs to be implentmented at the end for a exitting the window
				pygame.quit()
				sys.exit(0)

		pygame.display.flip() #Will allow what code that you put onto hear to be able to be recorded and placed onto the window created

if __name__ == '__main__':
	main()