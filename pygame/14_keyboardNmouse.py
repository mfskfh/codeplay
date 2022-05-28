# -*- coding: utf-8 -*-
import pygame
import random


pygame.init()


screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

character = pygame.image.load("pygame/source/character.png")

character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_xPos = (screen_width / 2) - (character_width / 2)
character_yPos = screen_height - character_height

character_toX = 0
character_toY = 0

enemy = pygame.image.load("pygame/source/ddong.png")

enemy_size = enemy.get_rect().size
enemy_width = enemy_size[0]
enemy_height = enemy_size[1]
enemy_xPos = (screen_width / 2) - (enemy_width / 2)
enemy_yPos = (screen_height / 2) - (enemy_height / 2)

enemy_toX = 0
enemy_toY = 0

ball = pygame.image.load("pygame/source/ball.png")

ball_size = ball.get_rect().size
ball_width = ball_size[0]
ball_height = ball_size[1]
ball_xPos = (screen_width / 2) - (enemy_width / 2)
ball_yPos = 0

ball_Xspeed = 3
ball_Yspeed = 3

pygame.display.set_caption("Mouse z")

# circle_xPos = 0
# circle_yPos = 0

clock = pygame.time.Clock()

running = True
while running:
    dt = clock.tick(30)

    for event in pygame.event.get():
        if event.type ==  pygame.QUIT:
            running = False
    
    ball_xPos += ball_Xspeed
    ball_yPos += ball_Yspeed

    if ball_xPos <= 0:
        ball_Xspeed *= (random.randint(1, 3) / ball_Xspeed)
        # ball_Xspeed = random.randint(3, 8)

    elif ball_xPos >= screen_width - ball_width:
        ball_Xspeed *= -1
        ball_Xspeed = -random.randint(3, 8)

    
    if ball_yPos <= 0:
        ball_Yspeed *= -1
        ball_Yspeed = random.randint(3, 8)

    elif ball_yPos >= screen_height - ball_height:
        ball_Yspeed *= -1
        ball_Yspeed = -random.randint(3, 8)

        # if event.type == pygame.MOUSEMOTION:
            # print("mousemotion")
            # print(pygame.mouse.get_pos())
        #     circle_xPos, circle_yPos = pygame.mouse.get_pos()
        #     # screen.fill((0, 0, 0))
        #     pygame.draw.circle(screen, (255, 255, 255), (circle_xPos, circle_yPos), 10)
        # if event.type == pygame.MOUSEBUTTONDOWN:
        #     print("mousebuttondown")
        #     print(pygame.mouse.get_pos())
        #     print(event.button)
        #     if event.button == 1:
        #         print("좌클")
        #     if event.button == 3:
        #         print("우클")
        #     if event.button == 2:
        #         print("휠클")
        #     if event.button == 4:
        #         print("휠업")
        #     if event.button == 5:
        #         print("휠다운")
        # if event.type == pygame.MOUSEBUTTONUP:
        #     print("mousebuttonup")

    screen.fill((0, 0, 0))
    screen.blit(ball, (ball_xPos, ball_yPos))

    print(ball_Xspeed, ball_Yspeed)
    pygame.display.update()

pygame.quit()