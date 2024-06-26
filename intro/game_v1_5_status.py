# Different game status
# Display scoring time
# Transforming surfaces (scale, rotate, etc)
    # Intro screen
# Add text title and instructions to start the game
# Add score when there is one to the initial game screen.


import pygame
from sys import exit

def display_score():
    current_time = int(pygame.time.get_ticks()/1000) - start_time
    score_surf = test_font.render(f'Score: {current_time}', False, (64,64,64))
    score_rect = score_surf.get_rect(center = (400,50))
    screen.blit(score_surf, score_rect)
    return current_time

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()
test_font = pygame.font.Font('font/Pixeltype.ttf', 50)
game_active = False
start_time = 0
score = 0

sky_surface = pygame.image.load('graphics/Sky.png').convert()
ground_surface = pygame.image.load('graphics/ground.png').convert()

#score_surf = test_font.render('My game', False, (64, 64, 64))
#score_rect = score_surf.get_rect(center = (400, 50))

snail_surf = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_rect = snail_surf.get_rect(bottomright = (600, 300))

player_surf = pygame.image.load('graphics/player/player_walk_1.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom = (80, 300))
player_gravity = 0

# Intro screen
player_stand = pygame.image.load('graphics/player/player_stand.png').convert_alpha()
#player_stand  = pygame.transform.scale(player_stand, (width,heigth))
player_stand  = pygame.transform.scale2x(player_stand)
#player_stand  = pygame.transform.rotozoom(player_stand,0,2)
player_stand_rect = player_stand.get_rect(center=(400,200))

title_surf = test_font.render('Pixel Runner', False, (111, 196, 169))
title_rect = title_surf.get_rect(center = (400, 80))

start_surf = test_font.render('Press space to run', False, (111, 196, 169))
start_rect = start_surf.get_rect(center = (400, 340))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if game_active:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if player_rect.collidepoint(event.pos) and player_rect.bottom >= 300:
                        player_gravity = -20
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rect.bottom >= 300:
                        player_gravity = -20
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                snail_rect.left = 800 
                start_time = int(pygame.time.get_ticks()/1000)

    if game_active:
        screen.blit(sky_surface, (0, 0))
        screen.blit(ground_surface, (0, 300))
        #pygame.draw.rect(screen, '#c0e8ec', score_rect)
        #pygame.draw.rect(screen, '#c0e8ec', score_rect, 10)
        #screen.blit(score_surf, score_rect)
        score = display_score()

        snail_rect.x -= 4
        if snail_rect.right <= 0: snail_rect.left = 800 
        screen.blit(snail_surf, snail_rect)

        # Player   
        player_gravity += 1
        player_rect.y += player_gravity
        if player_rect.bottom >= 300: player_rect.bottom = 300
        screen.blit(player_surf, player_rect) 

        # Collision
        if snail_rect.colliderect(player_rect):
            game_active = False
    
    else:
        screen.fill((94,129,162))
        screen.blit(player_stand, player_stand_rect)
        score_message = test_font.render(f'Your score: {score}', False, (111, 196, 169))
        score_message_rect = score_message.get_rect(center=(400,330))
        screen.blit(title_surf, title_rect)
        if score == 0:
            screen.blit(start_surf, start_rect)
        else:
            screen.blit(score_message, score_message_rect)

    pygame.display.update()
    clock.tick(60)