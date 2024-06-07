import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()
test_font = pygame.font.Font('font/Pixeltype.ttf', 50) # Import a font type.

# --------------- Important---------------#
# Note that the three surfaces are png files, but python works better with the converted() function applied to the
# png files. In the surface of the snail, we set all alpha values to zero for display improvement.
sky_surface = pygame.image.load('graphics/Sky.png').convert() # Imported image is placed in a differente surface.
ground_surface = pygame.image.load('graphics/ground.png').convert()
text_surface = test_font.render('My game', False, 'Black') # Second argument is for antialiasing. Smooth the edges of the text.
# Add a snail with an initial x position.
snail_surface = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_x_pos = 600

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit() 
    screen.blit(sky_surface, (0, 0))
    screen.blit(ground_surface, (0, 300))
    screen.blit(text_surface, (300, 50))
    
    # Every time the while loop is executed, snails position is updated.
    snail_x_pos -= 4
    if snail_x_pos < -100: snail_x_pos = 800
    screen.blit(snail_surface, (snail_x_pos, 250))

    pygame.display.update()
    clock.tick(60)