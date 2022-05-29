import pygame
import random


pygame.init()


screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))


bg_img = pygame.image.load("pygame\source\BallH\SpaceScreen.png").convert_alpha()
bg = pygame.transform.scale(bg_img, (640, 480))

ball_img = pygame.image.load("pygame\source\BallH\BallH_B.png").convert_alpha()
ball = pygame.transform.scale(ball_img, (80, 80))

ball_size = ball.get_rect().size
ball_width = ball_size[0]
ball_height = ball_size[1]
ball_xPos = (screen_width / 2) - (ball_width / 2)
ball_yPos = 0

ball_speed = random.randint(300, 500) / 100
ball_Xspeed = random.randint(100, 300) / 100
ball_Yspeed = random.randint(100, 300) / 100

bar_img = pygame.image.load("pygame\source\BallH\BarH_B.png").convert_alpha()
bar = pygame.transform.scale(bar_img, (180, 16))

bar_size = bar.get_rect().size
bar_width = bar_size[0]
bar_height = bar_size[1]
bar_xPos = (screen_width / 2) - (bar_width / 2)
bar_yPos = screen_height - screen_height / 16

pygame.display.set_caption("Ball Game")


clock = pygame.time.Clock()

game_font =  pygame.font.Font(None, 40)
score_font =  pygame.font.Font(None, 70)

total_time = 0
score = 0

start_ticks = pygame.time.get_ticks()
elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000


running = True
while running:
    dt = clock.tick(120)

    for event in pygame.event.get():
        if event.type ==  pygame.QUIT:
            running = False
        
        if event.type == pygame.MOUSEMOTION:
            bar_xPos = pygame.mouse.get_pos()[0] - (bar_width / 2)

    ball_xPos += ball_Xspeed
    ball_yPos += ball_Yspeed

    ball_speed = random.randint(300, 500) / 100

    if ball_xPos <= 0:
        # ball_Xspeed *= (random.randint(1, 3) / ball_Xspeed)
        ball_Xspeed = ball_speed

    elif ball_xPos >= screen_width - ball_width:
        ball_Xspeed *= -1
        ball_Xspeed = -ball_speed

    
    if ball_yPos <= 0:
        ball_Yspeed *= -1
        ball_Yspeed = ball_speed

    # elif ball_yPos >= screen_height - ball_height:
    #     ball_Yspeed *= -1
    #     ball_Yspeed = -random.randint(3, 5)


    ball_rect = ball.get_rect()
    ball_rect.left = ball_xPos
    ball_rect.top = ball_yPos

    bar_rect = bar.get_rect()
    bar_rect.left = bar_xPos
    bar_rect.top = bar_yPos


    if ball_yPos >= screen_height - ball_height:
        # pygame.time.delay(3000)
        pygame.quit()

    if ball_rect.colliderect(bar_rect):
        if ball_xPos <= ((bar_xPos / 2) + (bar_width / 2)):
            # print(ball_xPos, bar_xPos)
            ball_Xspeed = -ball_speed
        elif ball_xPos > ((bar_xPos / 2) + (bar_width /2)):
            # print(ball_xPos, bar_xPos)
            ball_Xspeed = ball_speed
        # if random.randint(1, 2) == 1:
        #     ball_Xspeed = random.randint(3, 5)
        # else:
        #     ball_Xspeed = -random.randint(3, 5)
        ball_Yspeed = -ball_speed
        score += 1
        ball_yPos = bar_yPos - bar_height - ball_height
    
    timertime = total_time + elapsed_time
    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000
    timer = game_font.render(str("Time : {0}".format(int(timertime))), True, (218, 165, 32))
    scoreboard = game_font.render(str("Score : {0}".format(score)), True, (137, 119, 173))


    screen.blit(bg, (0, 0))
    screen.blit(ball, (ball_xPos, ball_yPos))
    screen.blit(bar, (bar_xPos, bar_yPos))
    screen.blit(timer, (40, 40))
    screen.blit(scoreboard, (40, 70))


    pygame.display.update()

pygame.quit()