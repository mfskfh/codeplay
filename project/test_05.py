# -*- coding: utf-8 -*-

import pygame

pygame.init()

bg = pygame.image.load("project/source/bg/bg.png")
bg = pygame.transform.scale(bg, (640, 480))

patty = pygame.image.load("project/source/food/patty.png")
patty = pygame.transform.scale(patty, (200, 200))

pickle = pygame.image.load("project/source/food/pickle.png")
pickle = pygame.transform.scale(pickle, (200, 00))

bread_bottom = pygame.image.load("project/source/food/bread_bottom.png")
bread_bottom = pygame.transform.scale(bread_bottom, (200, 200))

days = pygame.image.load("project/source/days.png")
days = pygame.transform.scale(days, (100, 20))

guest1 = pygame.image.load("project/source/guest/h.su.png")
guest1 = pygame.transform.scale(guest1, (300, 300))

guest2 = pygame.image.load("project/source/guest/d.o.y.u.p.png")
guest2 = pygame.transform.scale(guest2, (300, 300))

guest3 = pygame.image.load("project/source/guest/je.h.yk.png")
guest3 = pygame.transform.scale(guest3, (300, 300))

guest4 = pygame.image.load("project/source/guest/se.ch.png")
guest4 = pygame.transform.scale(guest4, (300, 300))

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

foodbg = pygame.image.load("project/source/rdfoodbg.png")
foodbg = pygame.transform.scale(foodbg, (200, 120))


screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("즐겁다 햄버거집")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
    screen.blit(bg, (0, 0))
    screen.blit(ordermenu, (screen_width - 100, 0))
    screen.blit(days, (0, 40))
    screen.blit(manjok, (0, 20))
    screen.blit(money, (0, 0))
    screen.blit(guest4, (screen_width / 2 - 150, 7))
    screen.blit(foodbg, (screen_width / 2 - 70, 0))
    screen.blit(patty, (screen_width / 2 - 50, 5))
    screen.blit(bread_bottom, (screen_width / 2 - 105, 285))

    pygame.display.update()

pygame.quit()