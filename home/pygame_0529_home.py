# -*- coding: utf-8 -*-

import pygame


pygame.init()

screen_width = 640
screen_height = 200
screen = pygame.display.set_mode((screen_width, screen_height))


player_img = pygame.image.load("pygame/source/ddong_character.png").convert_alpha()
player = pygame.transform.scale(player_img, (80, 160))

player_size = player.get_rect().size
player_width = player_size[0]
player_height = player_size[1]
player_xPos = screen_width - player_width
player_yPos = screen_height - player_height

enemy_img = pygame.image.load("pygame/source/스카너.png").convert_alpha()
enemy = pygame.transform.scale(enemy_img, (300, 300))

enemy_size = enemy.get_rect().size
enemy_width = enemy_size[0]
enemy_height = enemy_size[1]
enemy_xPos = 0
enemy_yPos = screen_height - (enemy_height / 1.2)

bullet_img = pygame.image.load("pygame/source/ddong.png").convert_alpha()
bullet = pygame.transform.scale(bullet_img, (10, 10))

bullet_size = bullet.get_rect().size
bullet_width = bullet_size[0]
bullet_height = bullet_size[1]
bullet_xPos = -3000
bullet_yPos = 3000


clock = pygame.time.Clock()


running = True
while running:
    dt = clock.tick(120)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 

        if event.type == pygame.MOUSEBUTTONDOWN and bullet_xPos < 0:
            if event.button == 1:
                # print(2)
                screen.blit(bullet, (bullet_xPos, bullet_yPos))
                bullet_xPos = screen_width - player_width - bullet_width
                bullet_yPos = screen_height - (player_width / 2)

    
    bullet_xPos -= 10

    bullet_rect = bullet.get_rect()
    bullet_rect.left = bullet_xPos
    bullet_rect.top = player_yPos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_xPos
    enemy_rect.top = enemy_yPos

    if bullet_rect.colliderect(enemy_rect):
        enemy_img = pygame.image.load("pygame/source/restroom_bg.png").convert_alpha()
        enemy = pygame.transform.scale(enemy_img, (300, 300))
    
    else:
        enemy_img = pygame.image.load("pygame/source/스카너.png").convert_alpha()
        enemy = pygame.transform.scale(enemy_img, (300, 300))


    screen.fill((255, 255, 255))
    screen.blit(player, (player_xPos, player_yPos))
    screen.blit(enemy, (enemy_xPos, enemy_yPos))
    screen.blit(bullet, (bullet_xPos, bullet_yPos))


    pygame.display.update()

pygame.quit()