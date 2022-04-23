# -*- conding: utf-8 -*-

import pygame

pygame.init()

screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("똥피하기-코드플레이")

clock = pygame.time.Clock()

character_speed = 1

bg = pygame.image.load("pygame/source/bg.png")

ddong = pygame.image.load("pygame/source/ddong.png")
ddong_size = ddong.get_rect().size
ddong_width = ddong_size[0]
ddong_height = ddong_size[1]
ddong_xPos = (screen_width / 2) - (ddong_width / 2)
ddong_yPos = (screen_height / 2) - (ddong_height / 2)

player = pygame.image.load("pygame/source/superstrongplayer.png")
player_size = player.get_rect().size
player_width = player_size[0]
player_height = player_size[1]
player_xPos = screen_width - (player_width / 2)
player_yPos = screen_height - player_height

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(bg, (0,0))
    screen.blit(ddong, (ddong_xPos, ddong_yPos))
    screen.blit(player, (player_xPos, player_yPos))

    pygame.display.update()

pygame.quit()