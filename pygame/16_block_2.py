import pygame
import random

pygame.init()

#화면 크기 & 생성
screen_width = 640
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

clock = pygame.time.Clock()

#게임 이름
pygame.display.set_caption("맞짱")

#막대기 크기
bar_width = 150
bar_height = 26

#막대기 위치
bar_xPos =  screen_width / 2 - bar_width / 2
bar_yPos = screen_height - bar_height

bar_rect = pygame.Rect(bar_xPos, bar_yPos, bar_width, bar_height)

bar_toX = 0

#공 크기
ball_size = 20

#공 위치
ball_xPos = screen_width / 2
ball_yPos = screen_height / 2 - ball_size

#공 히트박스
ball_rect = pygame.Rect(ball_xPos, ball_yPos, ball_size * 2, ball_size * 2)
ball_rect.center = (ball_xPos, ball_yPos)

if random.randint(1, 2) == 1:
    ball_xSpeed = random.randint(1, 5)
else:
    ball_xSpeed = -random.randint(1, 5)
ball_ySpeed = random.randint(1, 5)

#벽돌 크기
block_width = screen_width / 10
block_height = 40

block_xPos = 0
block_yPos = 0

blocks = [[] for i in range(3)] #for문 앞에 복사할 문자를 넣으면 복사가 되는 ㅠ
block_color = [[], [], []]

for i in range(3):
    for j in range(10):
        blocks[i].append(pygame.Rect(j*block_width, i*block_height, block_width, block_height))
        block_color[i].append((random.randrange(256), random.randrange(256), random.randrange(256)))

pygame.mixer.init()

Sound_WallPop = pygame.mixer.Sound("pygame/source/Sound/Meow1.wav")
Sound_BarPop = pygame.mixer.Sound("pygame/source/Sound/Meow2.wav")
Sound_BGM = pygame.mixer.music.load("pygame/source/Sound/VideoGame1.wav")

pygame.mixer.music.play(-1)

running = True
while running:
    dt = clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                bar_toX = 5
            elif event.key == pygame.K_LEFT:
                bar_toX = -5
        
        if event.type == pygame.KEYUP:
            bar_toX = 0

    bar_xPos += bar_toX

    if ball_xPos - ball_size <= 0:
        ball_xSpeed = -ball_xSpeed
        Sound_WallPop.play()
    elif ball_xPos >= screen_width - ball_size:
        ball_xSpeed = - ball_xSpeed
        Sound_WallPop.play()

    if ball_yPos - ball_size <= 0:
        ball_xSpeed = -ball_xSpeed
        Sound_WallPop.play()
    elif ball_yPos >= screen_height - ball_size:
        ball_ySpeed = - ball_ySpeed
        Sound_WallPop.play()

    ball_xPos += ball_xSpeed
    ball_yPos += ball_ySpeed

    if bar_xPos < 0:
        bar_xPos = 0
    if bar_xPos + bar_width > screen_width:
        bar_xPos = screen_width - bar_width

    # print(ball_ySpeed)

    #배경그리기
    screen.fill((200, 200, 100))
    #막대기그리기
    bar_rect.left = bar_xPos
    pygame.draw.rect(screen, (90, 90, 255), bar_rect)
    #원그리기
    ball_rect.center = (ball_xPos, ball_yPos)
    pygame.draw.circle(screen, (255, 255, 255), (ball_xPos, ball_yPos), ball_size)

    if ball_rect.colliderect(bar_rect):
        ball_ySpeed = -ball_ySpeed
        Sound_BarPop.play()

    #벽돌 그리기
    for i in range(3):
        for j in range(10):
            if blocks[i][j]:
                pygame.draw.rect(screen, block_color[i][j], blocks[i][j])
                blocks[i][j].topleft = (j * block_width, i * block_height)

                if ball_rect.colliderect(blocks[i][j]):
                    ball_xSpeed *= -1
                    ball_ySpeed *= -1
                    blocks[i][j] = 0

    pygame.display.update()

#종료
pygame.quit()