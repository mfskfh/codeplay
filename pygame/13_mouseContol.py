# -*- coding: utf-8 -*-
import pygame



pygame.init()

screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Mouse z")

circle_xPos = 0
circle_yPos = 0

clock = pygame.time.Clock()

running = True
while running:
    dt = clock.tick(240)

    for event in pygame.event.get():
        if event.type ==  pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEMOTION:
            # print("mousemotion")
            # print(pygame.mouse.get_pos())
            circle_xPos, circle_yPos = pygame.mouse.get_pos()
            # screen.fill((0, 0, 0))
            pygame.draw.circle(screen, (255, 255, 255), (circle_xPos, circle_yPos), 10)
        if event.type == pygame.MOUSEBUTTONDOWN:
            print("mousebuttondown")
            print(pygame.mouse.get_pos())
            print(event.button)
            if event.button == 1:
                print("좌클")
            if event.button == 3:
                print("우클")
            if event.button == 2:
                print("휠클")
            if event.button == 4:
                print("휠업")
            if event.button == 5:
                print("휠다운")
        # if event.type == pygame.MOUSEBUTTONUP:
        #     print("mousebuttonup")

    pygame.display.update()

pygame.quit()