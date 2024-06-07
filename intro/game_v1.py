import pygame
from sys import exit

pygame.init() # Starts pygame
screen = pygame.display.set_mode((800, 400))# Creates a display surface. This is unique. (width, height)
pygame.display.set_caption('Runner')
clock = pygame.time.Clock() # To control the frame rate

test_surface = pygame.Surface((100, 200)) # Regular surface embedded in the display. 
test_surface.fill('Red')

while True:
    for event in pygame.event.get(): # any event by the user
        if event.type == pygame.QUIT:
            pygame.quit()
            exit() # Exit all, even the while loop.
    # draw all elements
    # update everything
    screen.blit(test_surface, (200, 100)) # blit stands for block image transfer.

    pygame.display.update() # updates the screen surface.
    clock.tick(60) # Tells the loop to not run faster than 60 times per second. 