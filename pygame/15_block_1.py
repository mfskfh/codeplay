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

bar_toX = 0

#공 크기
ball_size = 20

#공 위치
ball_xPos = screen_width / 2
ball_yPos = screen_height / 2 - ball_size

#공 히트박스
ball_rect = pygame.Rect(ball_xPos, ball_yPos, ball_size * 2, ball_size * 2)
ball_rect_center = (ball_xPos, ball_yPos)

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

    ball_xPos += ball_xSpeed
    ball_yPos += ball_ySpeed

    if bar_xPos < 0:
        bar_xPos = 0
    if bar_xPos + bar_width > screen_width:
        bar_xPos = screen_height - bar_width

    #배경그리기
    screen.fill((200, 200, 100))
    #막대기그리기
    pygame.draw.rect(screen, (90, 90, 255), (bar_xPos, bar_yPos, bar_width, bar_height))
    #원그리기
    pygame.draw.circle(screen, (255, 255, 255), (ball_xPos, ball_yPos), ball_size)

    #벽돌 그리기
    for i in range(3):
        for j in range(10):
            pygame.draw.rect(screen, block_color[i][j], blocks[i][j])

    pygame.display.update()

#종료
pygame.quit()