# -*- coding: utf-8 -*-

import pygame
import random

pygame.init()

score = 0

screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("똥피하기-코드플레이")

clock = pygame.time.Clock()

character_speed = 0.3

bg = pygame.image.load("pygame/source/restroom_bg.png")

character = pygame.image.load("pygame/source/ddong_character.png")
enemy = pygame.image.load("pygame/source/ddong.png")

character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_xPos = (screen_width / 2) - (character_width / 2)
character_yPos = screen_height - character_height

enemy_size = enemy.get_rect().size
enemy_width = enemy_size[0]
enemy_height = enemy_size[1]
enemy_xPos = (screen_width / 2) - (enemy_width / 2)
enemy_yPos = 0

game_font =  pygame.font.Font(None, 40)
score_font =  pygame.font.Font(None, 70)

total_time = 0

start_ticks = pygame.time.get_ticks()


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
# to_y = 0

enemy_to_y = random.randint(1, 5)

running = True
while running:
    dt = clock.tick(120)
    # print("fps : " + str(clock.get_fps()))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed
            # elif event.key == pygame.K_UP:
            #     to_y -= character_speed
            # elif event.key == pygame.K_DOWN:
            #     to_y += character_speed
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            # elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
            #     to_y = 0

    character_xPos += to_x * dt
    # character_yPos += to_y * dt

    enemy_yPos += enemy_to_y

    if enemy_yPos >= screen_height:
        enemy_yPos = 0
        enemy_xPos = random.randint(0, (screen_width - enemy_width))
        enemy_to_y = random.randint(1, 5)
        score += 1

    if character_xPos < 0:
        character_xPos = 0
    elif character_xPos > screen_width - character_width:
        character_xPos = screen_width - character_width
    
    # if character_yPos < 0:
    #     character_yPos = 0
    # elif character_yPos > screen_height - character_height:
    #     character_yPos = screen_height - character_height

    character_rect = character.get_rect()
    character_rect.left = character_xPos
    character_rect.top = character_yPos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_xPos
    enemy_rect.top = enemy_yPos

    if character_rect.colliderect(enemy_rect):
        score_text = score_font.render(("Score : %s" % score), True, (0, 0, 0))
        screen.blit(score_text, ((screen_width / 2), (screen_height / 2)))
        pygame.display.update()
        pygame.time.delay(3000)
        running = False

    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000
    timer = game_font.render(str(int(total_time + elapsed_time)), True, (0, 0, 0))

    screen.blit(bg, (0,0))
    screen.blit(enemy, (enemy_xPos, enemy_yPos))
    screen.blit(character, (character_xPos, character_yPos))
    screen.blit(timer, (10, 10))

    pygame.display.update()

# pygame.time.delay(1000)

pygame.quit()