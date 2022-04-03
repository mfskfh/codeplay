# -*- coding: utf-8 -*-

import pygame

# 1. 게임 초기화

pygame.init()

# 2. 게임창 옵션설정

size = [400, 700]
screen = pygame.display.set_mode(size)

title = "GayGame"
pygame.display.set_caption(title)

# 3. 게임 내의 필요한 설정

class obj:
    def __init__(self):
        self.x = 0
        self.y = 0
    def put_img(self, address):
        if address[-3:] == "png":
            self.img = pygame.image.load(address).convert_alpha()
        else:
            self.img = pygame.image.load(address)
            self.sx, self.sy = self.img.get_size()
    def change_size(self, sx, sy):
        self.img = pygame.transform.scale(self.img, (sx, sy))
        self.sx, self.sy = self.img.get_size()
    def show(self):
        screen.blit(self.img, (self.x, self.y))

HCat = obj()
HCat.put_img("C:/Users/jhyan/Videos/꼬량이/cat_face.png")
HCat.change_size(90, 90)
HCat.x = round(size[0]/2 -HCat.sx/2)
HCat.y = size[1] -HCat.sy -8

clock = pygame.time.Clock()
color = (0, 0, 0)

# 4. 메인이벤트

SB = 0
while SB == 0:
    
    # - FPS 설정
    clock.tick(60)

    # - 입력 감지
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            SB = 1
    # - 입력/시간에 따른 변화
    # - 그리기

    screen.fill(color)
    HCat.show()

    # - 업데이트

    pygame.display.flip()

# 5. 게임종료

pygame.quit()