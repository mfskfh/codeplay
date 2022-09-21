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
# 0 : 인트로 , 1 : 인트로 스토리 , 2 : 튜토리얼 ,3 : 게임진행 , 4 : 하루 끝 , 5 : 게임 끝
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
    def get_rect(self):
        self.rect = self.img.get_rect()
        self.rect.left = self.x
        self.rect.top = self.y


#배경
intro_bg = imageload()
intro_bg.put_img("project/source/bg/gamestart.png")

story_bg = imageload()
story_bg.put_img("project/source/bg/story.png")

tutorial_bg = imageload()
tutorial_bg.put_img("project/source/bg/tutorial.png")

game_bg = imageload()
game_bg.put_img("project/source/bg/bg.png")

#UI
start_button = imageload()
start_button.put_img("project/source/ui/gamestartbt.png")
start_button.change_size(180, 60)
start_button.x = (screen_width / 2) - (start_button.img.get_size()[0] / 2)
start_button.y = 3 * screen_height / 4
start_button.get_rect()

ok_button = imageload()
ok_button.put_img("project/source/ui/okbt.png")
ok_button.change_size(180, 60)
ok_button.x = screen_width - ok_button.img.get_size()[0] - 10
ok_button.y = screen_height - ok_button.img.get_size()[1] - 10
ok_button.get_rect()


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if start_button.rect.collidepoint(event.pos) == True:
                if game_progress_state == 0:
                    game_progress_state = 1
                    story_bg.show()
                    ok_button.show()
            if ok_button.rect.collidepoint(event.pos) == True:
                if game_progress_state == 1:
                    tutorial_bg.show()
                    ok_button.show()
                if game_progress_state == 2:
                    game_progress_state = 3
                    game_bg.show()
        if event.type == pygame.MOUSEBUTTONUP:
            if game_progress_state == 1:
                game_progress_state == 2
                print(1)
                print(game_progress_state)
                


        

        

    if game_progress_state == 0:
        intro_bg.show()
        start_button.show()
    if game_progress_state == 1:
        pass

    pygame.display.update()

pygame.quit()