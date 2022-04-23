# -*- coding: utf-8 -*-

import pygame

pygame.init()

screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("똥피하기-코드플레이")

clock = pygame.time.Clock()

character_speed = 1

bg = pygame.image.load("pygame/source/bg.png")

character = pygame.image.load("pygame/source/character.png")

character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_xPos = (screen_width / 2) - (character_width / 2)
character_yPos = screen_height - character_height

# character_xPos = 0
# character_yPos = 0

# character_xPos = screen_width - character_width
# character_yPos = 0

# character_xPos = 0
# character_yPos = screen_height - character_height

# character_xPos = screen_width - character_width
# character_yPos = screen_height - character_height

# character_xPos = (screen_width / 2) - (character_width / 2)
# character_yPos = 0

# character_xPos = (screen_width / 2) - (character_width / 2)
# character_yPos = (screen_height / 2) - (character_height / 2)

to_x = 0
to_y = 0

running = True
while running:
    dt = clock.tick(120)
    print("fps : " + str(clock.get_fps()))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed
            elif event.key == pygame.K_UP:
                to_y -= character_speed
            elif event.key == pygame.K_DOWN:
                to_y += character_speed
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0

    character_xPos += to_x * dt
    character_yPos += to_y * dt

    if character_xPos < 0:
        character_xPos = 0
    elif character_xPos > screen_width - character_width:
        character_xPos = screen_width - character_width
    
    if character_yPos < 0:
        character_yPos = 0
    elif character_yPos > screen_height - character_height:
        character_yPos = screen_height - character_height

    screen.blit(bg, (0,0))
    screen.blit(character, (character_xPos, character_yPos))
    pygame.display.update()

pygame.quit()