# -*- coding: utf-8 -*-

import pygame

pygame.init()

#화면 설정
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))

#게임 데이터
satisfaction = 10
money = 10000
passed_days = 0
passed_guest = 0

order_guest = 0
order_menu = 0
random_things = 0
choose_things = []
# 0 : 인트로 , 1 : 게임진행 , 2 : 하루 끝 , 3 : 게임 끝
game_progress_state = 0


class imageload:
    def __init__(self):
        self.x = 0
        self.y = 0
    def put_img(self, address):
        self.img = pygame.image.load(address)
    def change_size(self, sx, sy):
        self.img = pygame.transform.scale(self.img, (sx, sy))
        self.sx, self.sy = self.img.get_size()
    def show(self):
        screen.blit(self.img, (self.x, self.y))

#배경
intro_bg = imageload()
intro_bg.put_img("project/source/bg/gamestart.png")

#UI
start_button = imageload()
start_button.put_img("project/source/ui/gamestartbt.png")
start_button.change_size(180, 60)
start_button.x = (screen_width / 2) - (start_button.img.get_size()[0] / 2)
start_button.y = 3 * screen_height / 4

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        

        

    intro_bg.show()
    start_button.show()

    pygame.display.update()

pygame.quit()