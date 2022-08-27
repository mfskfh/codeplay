# -*- coding: utf-8 -*-

import pygame
import random

pygame.init()

screen_width = 1920
screen_height = 1080
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("즐겁다 햄버거집")

clock = pygame.time.Clock()

running = True
while running:
    dt = clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    pygame.display.update()

pygame.quit()