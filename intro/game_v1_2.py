import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()
test_font = pygame.font.Font('font/Pixeltype.ttf', 50)

sky_surface = pygame.image.load('graphics/Sky.png').convert()
ground_surface = pygame.image.load('graphics/ground.png').convert()
text_surface = test_font.render('My game', False, 'Black')

snail_surf = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_rect = snail_surf.get_rect(bottomright = (600, 300))

player_surf = pygame.image.load('graphics/player/player_walk_1.png').convert_alpha()
# The following creates a rectangle, which is very useful for surface positioning and
# is also useful for collisions.
player_rect = player_surf.get_rect(midbottom = (80, 300)) # Takes a surface and draws a rectangle around it.
# sprite class combines the two above commands.

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        #if event.type == pygame.MOUSEMOTION: 
        #    print(event.pos) # see the mouse position
        if event.type == pygame.MOUSEBUTTONDOWN:
            print('mouse down') # see if mouse button is down
        if event.type == pygame.MOUSEBUTTONUP:
            print('mouse up') # see if mouse button is released.
        
        # My way 
        #mouse_pos = pygame.mouse.get_pos()
        #if (player_rect.collidepoint(mouse_pos)):
        #    print('collision')

        # Another way
        if event.type == pygame.MOUSEMOTION:
            if player_rect.collidepoint(event.pos): print('collision')
    screen.blit(sky_surface, (0, 0))
    screen.blit(ground_surface, (0, 300))
    screen.blit(text_surface, (300, 50))
    snail_rect.x -= 4
    if snail_rect.right <= 0: snail_rect.left = 800
    screen.blit(snail_surf, snail_rect)
    #player_rect.left += 1
    #print(player_rect.left)
    screen.blit(player_surf, player_rect) # Now the player surface is placed where the player rectangle is.

    #if player_rect.colliderect(snail_rect): # returns 0 or 1. Python tests for true, is not necessary to write if ... == 1.
    #    print('collision') 

    # With the following code one can check if the mouse is being pressed and which of the buttons is pressed.
    #mouse_pos = pygame.mouse.get_pos()
    #if (player_rect.collidepoint(mouse_pos)):
    #    print(pygame.mouse.get_pressed())

    pygame.display.update()
    clock.tick(60)