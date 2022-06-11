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
ball_yPos = (screen_height / 2) - (ball_height / 2)

ball_speed = random.randint(300, 500) / 100
if random.randint(1, 2) == 1:
    ball_Xspeed = random.randint(100, 300) / 100
else:
    ball_Xspeed = -random.randint(100, 300) / 100
if random.randint(1, 2) == 1:
    ball_Yspeed = random.randint(100, 300) / 100
else:
    ball_Yspeed = -random.randint(100, 300) / 100

bar_img = pygame.image.load("pygame\source\BallH\BarH_B.png").convert_alpha()
bar = pygame.transform.scale(bar_img, (180, 16))

bar_size = bar.get_rect().size
bar_width = bar_size[0]
bar_height = bar_size[1]
bar_xPos = (screen_width / 2) - (bar_width / 2)
bar_yPos = screen_height - screen_height / 16

bar_toX = 0

bar2 = pygame.transform.scale(bar_img, (180, 16))

bar2_size = bar2.get_rect().size
bar2_width = bar2_size[0]
bar2_height = bar2_size[1]
bar2_xPos = (screen_width / 2) - (bar2_width / 2)
bar2_yPos = screen_height / 16

bar2_toX = 0

Sound_GameOver = pygame.mixer.Sound("pygame/source/Sound/GameOver.wav")
Sound_BarPop = pygame.mixer.Sound("pygame/source/Sound/BarPop.wav")
Sound_WallPop = pygame.mixer.Sound("pygame/source/Sound/WallPop.wav")
Sound_BGM = pygame.mixer.music.load("pygame/source/Sound/SpaceBGM.wav")

pygame.display.set_caption("Ball Game")


clock = pygame.time.Clock()

game_font =  pygame.font.Font(None, 40)
score_font =  pygame.font.Font(None, 70)
winner_font =  pygame.font.Font(None, 70)

winner = 0
winnerboard = winner_font.render("Winner : {0}".format(winner), True, (255, 255, 255))

total_time = 0
score = 0

start_ticks = pygame.time.get_ticks()
elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000

pygame.mixer.music.play(-1)

running = True
while running:
    dt = clock.tick(120)

    for event in pygame.event.get():
        if event.type ==  pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                bar_toX = -5
            elif event.key == pygame.K_RIGHT:
                bar_toX = 5
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                bar2_toX = -5
            elif event.key == pygame.K_d:
                bar2_toX = 5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                bar_toX = 0
            if event.key == pygame.K_a or event.key == pygame.K_d:
                bar2_toX = 0
        
        # if event.type == pygame.MOUSEMOTION:
        #     bar_xPos = pygame.mouse.get_pos()[0] - (bar_width / 2)

    bar_xPos += bar_toX
    bar2_xPos += bar2_toX

    ball_xPos += ball_Xspeed
    ball_yPos += ball_Yspeed

    ball_speed = random.randint(300, 500) / 100

    if bar_xPos <= 0:
        bar_xPos = 0
    elif bar_xPos >= screen_width - bar_width:
        bar_xPos = screen_width - bar_width

    if ball_xPos <= 0:
        # ball_Xspeed *= (random.randint(1, 3) / ball_Xspeed)
        ball_Xspeed = ball_speed
        Sound_WallPop.play()

    elif ball_xPos >= screen_width - ball_width:
        ball_Xspeed *= -1
        ball_Xspeed = -ball_speed
        Sound_WallPop.play()

    
    # if ball_yPos <= 0:
    #     ball_Yspeed *= -1
    #     ball_Yspeed = ball_speed
    #     Sound_WallPop.play()

    # elif ball_yPos >= screen_height - ball_height:
    #     ball_Yspeed *= -1
    #     ball_Yspeed = -random.randint(3, 5)


    ball_rect = ball.get_rect()
    ball_rect.left = ball_xPos
    ball_rect.top = ball_yPos

    bar_rect = bar.get_rect()
    bar_rect.left = bar_xPos
    bar_rect.top = bar_yPos

    bar2_rect = bar2.get_rect()
    bar2_rect.left = bar2_xPos
    bar2_rect.top = bar2_yPos


    if ball_yPos >= screen_height - ball_height:
        # pygame.time.delay(3000)
        Sound_GameOver.play()
        winner = 1
        screen.blit(winnerboard, ((screen_width / 2), (screen_height / 2)))
        pygame.display.update()
        pygame.time.delay(1430)
        pygame.quit()

    if ball_yPos <= 0:
        # pygame.time.delay(3000)
        Sound_GameOver.play()
        winner = 2
        screen.blit(winnerboard, ((screen_width / 2), (screen_height / 2)))
        pygame.display.update()
        pygame.time.delay(1430)
        pygame.quit()

    if ball_rect.colliderect(bar_rect):
        # if ball_xPos <= ((bar_xPos / 2) + (bar_width / 2)):
            # print(ball_xPos, bar_xPos)
            # ball_Xspeed = -ball_speed
        # elif ball_xPos > ((bar_xPos / 2) + (bar_width /2)):
            # print(ball_xPos, bar_xPos)
            # ball_Xspeed = ball_speed
        if random.randint(1, 2) == 1:
            ball_Xspeed = random.randint(3, 5)
        else:
            ball_Xspeed = -random.randint(3, 5)
        ball_Yspeed = -ball_speed
        score += 1
        ball_yPos = bar_yPos - bar_height - ball_height
        Sound_BarPop.play()

    if ball_rect.colliderect(bar2_rect):
        # if ball_xPos <= ((bar_xPos / 2) + (bar_width / 2)):
            # print(ball_xPos, bar_xPos)
            # ball_Xspeed = -ball_speed
        # elif ball_xPos > ((bar_xPos / 2) + (bar_width /2)):
            # print(ball_xPos, bar_xPos)
            # ball_Xspeed = ball_speed
        if random.randint(1, 2) == 1:
            ball_Xspeed = random.randint(3, 5)
        else:
            ball_Xspeed = -random.randint(3, 5)
        ball_Yspeed = ball_speed
        score += 1
        ball_yPos = bar2_yPos + bar2_height + 10
        Sound_BarPop.play()

    
    timertime = total_time + elapsed_time
    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000
    timer = game_font.render(str("Time : {0}".format(int(timertime))), True, (218, 165, 32))
    scoreboard = game_font.render(str("Score : {0}".format(score)), True, (137, 119, 173))


    screen.blit(bg, (0, 0))
    screen.blit(ball, (ball_xPos, ball_yPos))
    screen.blit(bar, (bar_xPos, bar_yPos))
    screen.blit(bar2, (bar2_xPos, bar2_yPos))
    screen.blit(timer, (40, 40))
    screen.blit(scoreboard, (40, 70))


    pygame.display.update()

pygame.quit()