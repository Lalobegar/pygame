import pygame, sys
from settings import *
from level import Level

class Game:
    def __init__(self):

        # general setup
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGTH)) # Create a display surface
        pygame.display.set_caption('Zeldalike')
        self.clock = pygame.time.Clock() # Create a clock

        self.level = Level() # Create an instance of the level class
    
    def run(self):
        while True:
            for event in pygame.event.get(): # Check if we close the game
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            self.screen.fill('black') # Fill the screen with black
            self.level.run() # call the method run of the class Level
            pygame.display.update()
            self.clock.tick(FPS)

if __name__ == '__main__': # check if the file is the main
    game = Game() # create an instance of the game class
    game.run() # call the method run of class