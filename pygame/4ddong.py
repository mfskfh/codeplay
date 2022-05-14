# -*- coding: utf-8 -*-

import pygame
import random

pygame.init()

score = 0

screen_width = 800
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("똥피하기-코드플레이")

clock = pygame.time.Clock()

character_speed = 0.3

bg = pygame.image.load("pygame/source/4ddong/bg1.png")

character = pygame.image.load("pygame/source/4ddong/player1.png")

item = pygame.image.load("pygame/source/4ddong/item.png")

enemy1 = pygame.image.load("pygame/source/4ddong/ddong1.png")
enemy2 = pygame.image.load("pygame/source/4ddong/ddong1.png")
enemy3 = pygame.image.load("pygame/source/4ddong/ddong1.png")
enemy4 = pygame.image.load("pygame/source/4ddong/ddong1.png")

character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_xPos = (screen_width / 2) - (character_width / 2)
character_yPos = (screen_height / 2) - (character_height / 2)

enemy1_size = enemy1.get_rect().size
enemy1_width = enemy1_size[0]
enemy1_height = enemy1_size[1]
enemy1_xPos = random.randint(0, (screen_width - (enemy1_width / 2)))
enemy1_yPos = 0

enemy2_size = enemy2.get_rect().size
enemy2_width = enemy2_size[0]
enemy2_height = enemy2_size[1]
enemy2_xPos = random.randint(0, (screen_width -(enemy2_width / 2)))
enemy2_yPos = screen_height

enemy3_size = enemy3.get_rect().size
enemy3_width = enemy3_size[0]
enemy3_height = enemy3_size[1]
enemy3_xPos = 0
enemy3_yPos = random.randint(0, (screen_height - enemy3_height / 2))

enemy4_size = enemy4.get_rect().size
enemy4_width = enemy4_size[0]
enemy4_height = enemy4_size[1]
enemy4_xPos = screen_width
enemy4_yPos = random.randint(0, (screen_height - enemy3_height / 2))

item_size = item.get_rect().size
item_width = item_size[0]
item_height = item_size[1]
item_xPos = random.randint(0, (screen_width - item_width))
item_yPos = random.randint(0, (screen_height - item_height))

item_delay = (random.randint(1, 4) * 200)
item_delay_time = 0

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
to_y = 0

enemy1_to_y = random.randint(3, 5)
enemy2_to_y = random.randint(3, 5)
enemy3_to_x = random.randint(3, 5)
enemy4_to_x = random.randint(3, 5)

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

    enemy1_yPos += enemy1_to_y
    enemy2_yPos -= enemy2_to_y
    enemy3_xPos += enemy3_to_x
    enemy4_xPos -= enemy4_to_x

    if enemy1_yPos >= screen_height:
        enemy_yPos = 0
        enemy_xPos = random.randint(0, (screen_width - enemy1_width))
        enemy_to_y = random.randint(1, 5)
        # score += 1

    if enemy2_yPos <= (0 - character_height):
        enemy2_yPos = screen_height
        enemy2_xPos = random.randint(0, (screen_width - enemy2_width))
        enemy2_to_y = random.randint(1, 5)
        # score += 1

    if enemy3_xPos >= screen_width:
        enemy3_yPos = random.randint(0, (screen_height - enemy3_width))
        enemy3_xPos = 0
        enemy3_to_y = random.randint(1, 5)

    if enemy4_xPos <= (0 - enemy4_width):
        enemy4_yPos = random.randint(0, (screen_height - enemy4_width))
        enemy4_xPos = screen_width
        enemy4_to_y = random.randint(1, 5)

    if character_xPos < 0:
        character_xPos = 0
    elif character_xPos > screen_width - character_width:
        character_xPos = screen_width - character_width
    
    if character_yPos < 0:
        character_yPos = 0
    elif character_yPos > screen_height - character_height:
        character_yPos = screen_height - character_height

    character_rect = character.get_rect()
    character_rect.left = character_xPos
    character_rect.top = character_yPos

    enemy1_rect = enemy1.get_rect()
    enemy1_rect.left = enemy1_xPos
    enemy1_rect.top = enemy1_yPos

    enemy2_rect = enemy2.get_rect()
    enemy2_rect.left = enemy2_xPos
    enemy2_rect.top = enemy2_yPos

    enemy3_rect = enemy3.get_rect()
    enemy3_rect.left = enemy3_xPos
    enemy3_rect.top = enemy3_yPos

    enemy4_rect = enemy4.get_rect()
    enemy4_rect.left = enemy4_xPos
    enemy4_rect.top = enemy4_yPos

    item_rect = item.get_rect()
    item_rect.left = item_xPos
    item_rect.top = item_yPos

    if character_rect.colliderect(enemy1_rect) or character_rect.colliderect(enemy2_rect) or character_rect.colliderect(enemy3_rect) or character_rect.colliderect(enemy4_rect):
        timescore_text = score_font.render(("Time : %s Sec" % int(elapsed_time)), True, (0, 0, 0))
        screen.blit(timescore_text, ((screen_width / 3), (screen_height / 2)))
        score_text = score_font.render(("Score : %s" % score), True, (0, 0, 0))
        screen.blit(score_text, ((screen_width / 3), (screen_height / 3)))
        pygame.display.update()
        pygame.time.delay(3000)
        running = False

    if character_rect.colliderect(item_rect):
        score += 1
        item_xPos = 70000
        item_yPos = 70000
    
    if item_xPos == 70000:
        item_delay_time += 1

    if item_delay == item_delay_time:
        item_delay_time = 0
        item_xPos = random.randint(0, (screen_width - item_width / 2))
        item_yPos = random.randint(0, (screen_height - item_height / 2))

    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000
    timer = game_font.render(str(int(total_time + elapsed_time)), True, (0, 0, 0))
    scoreboard = game_font.render(str("Score : {0}".format(score)), True, (0, 0, 0))

    screen.blit(bg, (0,0))
    screen.blit(enemy1, (enemy1_xPos, enemy1_yPos))
    screen.blit(enemy2, (enemy2_xPos, enemy2_yPos))
    screen.blit(enemy3, (enemy3_xPos, enemy3_yPos))
    screen.blit(enemy4, (enemy4_xPos, enemy4_yPos))
    screen.blit(character, (character_xPos, character_yPos))
    screen.blit(item, (item_xPos, item_yPos))
    screen.blit(timer, (10, 10))
    screen.blit(scoreboard, (10, 40))

    # print(item_delay_time)
    # print(score)    

    pygame.display.update()

# pygame.time.delay(1000)

pygame.quit()