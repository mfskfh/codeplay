# -*- coding: utf-8 -*-

import pygame

pygame.init()

patty = pygame.image.load("project/source/patty.png")
patty = pygame.transform.scale(patty, (100, 100))

days = pygame.image.load("project/source/days.png")
days = pygame.transform.scale(days, (100, 20))

guest = pygame.image.load("project/source/guest.png")
guest = pygame.transform.scale(guest, (300, 300))

ordermenu = pygame.image.load("project/source/orthermenu.png")
ordermenu = pygame.transform.scale(ordermenu, (100, 480))

mademenu = pygame.image.load("project/source/madefood.png")
mademenu = pygame.transform.scale(mademenu, (100, 100))

manjok = pygame.image.load("project/source/manjok.png")
manjok = pygame.transform.scale(manjok, (100, 20))

money = pygame.image.load("project/source/money.png")
money = pygame.transform.scale(money, (100, 20))

money = pygame.image.load("project/source/money.png")
money = pygame.transform.scale(money, (100, 20))


screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("즐겁다 햄버거집")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))
            
    screen.blit(patty, (screen_width / 2 - 50, screen_height / 24))
    screen.blit(ordermenu, (screen_width - 100, 60))
    screen.blit(days, (screen_width - 100, 40))
    screen.blit(manjok, (screen_width - 100, 20))
    screen.blit(money, (screen_width - 100, 0))
    screen.blit(guest, (screen_width / 2 - 150, screen_height / 2 - 150))
    screen.blit(mademenu, (screen_width / 2 - 100, 2 * (screen_height / 3)))

    pygame.display.update()

pygame.quit()