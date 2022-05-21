# -*- coding: utf-8 -*-
import pygame



pygame.init()

screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("z")


clock = pygame.time.Clock()

running = True
while running:
    dt = clock.tick(30)

    for event in pygame.event.get():
        if event.type ==  pygame.QUIT:
            running = False
    screen.fill((255, 255, 255))

    #그릴 대상, 색 , 시작좌표 , 끝좌표 , 굵기
    pygame.draw.line(screen, (255, 0, 0), ((screen_width / 2), 0), ((screen_width / 2), (screen_height - (screen_height / 3))), 30)
    pygame.draw.line(screen, (0, 255, 0), (0, (screen_height - (screen_height / 3))), (screen_width, (screen_height - (screen_height / 3))), 30)

    #그릴 대상 , 색 , 좌표 , 반지름 , 굵기(선굵기를 생략하면 다 채움 ㅋ)
    pygame.draw.circle(screen, (0, 255, 0), (screen_width / 2, screen_height /2), 100)
    pygame.draw.circle(screen, (255, 0, 0), (screen_width / 2, screen_height /2), 100 ,15)

    #그릴 대상 , 색 , 시작좌표 , 가로 길이 , 세로 길이 , 굵기(선굵기를 생략하면 다 채움 ㅋ)
    pygame.draw.rect(screen, (55, 55, 255), (screen_width /2, screen_height / 2, 100, 100))
    pygame.draw.rect(screen, (155, 155, 55), (screen_width /2, screen_height / 2, 100, 100), 5)

    #그릴 대상 , 색 , 시작좌표 , 가로 길이 , 세로 길이 , 굵기(선굵기를 생략하면 다 채움 ㅋ)
    pygame.draw.ellipse(screen, (55, 55, 55), (screen_width / 2, screen_height / 2, 1000000, 100))
    pygame.draw.ellipse(screen, (155, 155, 155), (screen_width / 2, screen_height / 2, 100, 100), 5)

    #그릴 대상, 색 , n번쨰 꼭짓점 좌표 , 굵기(선굵기를 생략하면 다 채움 ㅋ)
    pygame.draw.polygon(screen, (123, 13, 43), ([100, 0],[0, 200], [200, 200]))
    pygame.draw.polygon(screen, (123, 13, 43), ([100, 0], [0, 100], [0, 200], [100, 300], [200, 200], [200, 100]))

    for i in range(0, screen_width, 30):
        pygame.draw.line(screen, (0, 0, 255), (i, 0), (i, screen_height))
    for i in range(0, screen_height, 30):
        pygame.draw.line(screen, (0, 0, 255), (0, i), (screen_width, i))

    pygame.display.update()

pygame.quit()