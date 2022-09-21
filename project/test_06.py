# -*- coding: utf-8 -*-

import pygame
import random
from data_01 import *

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
okbt_press_state = 0
guest_presence_or_absence = 0

def food_all_alpha(a):
        food_01.img.set_alpha(a) 
        food_02.img.set_alpha(a)
        food_03.img.set_alpha(a) 
        food_04.img.set_alpha(a) 
        # food_05.img.set_alpha(a) 
        food_06.img.set_alpha(a) 
        food_07.img.set_alpha(a) 
        food_08.img.set_alpha(a) 
        food_09.img.set_alpha(a) 

def guest_all_alpha(a):
        guests_01.img.set_alpha(a) 
        guests_02.img.set_alpha(a)
        guests_03.img.set_alpha(a) 
        guests_04.img.set_alpha(a) 
        guests_05.img.set_alpha(a)
        guests_06.img.set_alpha(a) 
        guests_07.img.set_alpha(a) 



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

#손님
guests_01 = imageload()
guests_01.put_img("project/source/guest/hsu.png")
guests_01.change_size(300, 300)
guests_01.x = (screen_width / 2) - (guests_01.img.get_size()[0] / 2)
guests_01.y = 7
guests_01.get_rect()
guests_01.img.set_alpha(0)

guests_02 = imageload()
guests_02.put_img("project/source/guest/doyup.png")
guests_02.change_size(300, 300)
guests_02.x = (screen_width / 2) - (guests_02.img.get_size()[0] / 2)
guests_02.y = 7
guests_02.get_rect()
guests_02.img.set_alpha(0)

guests_03 = imageload()
guests_03.put_img("project/source/guest/jwoo.png")
guests_03.change_size(300, 300)
guests_03.x = (screen_width / 2) - (guests_03.img.get_size()[0] / 2)
guests_03.y = 7
guests_03.get_rect()
guests_03.img.set_alpha(0)

guests_04 = imageload()
guests_04.put_img("project/source/guest/jehyk.png")
guests_04.change_size(300, 300)
guests_04.x = (screen_width / 2) - (guests_04.img.get_size()[0] / 2)
guests_04.y = 7
guests_04.get_rect()
guests_04.img.set_alpha(0)

guests_05 = imageload()
guests_05.put_img("project/source/guest/mjae.png")
guests_05.change_size(300, 300)
guests_05.x = (screen_width / 2) - (guests_05.img.get_size()[0] / 2)
guests_05.y = 7
guests_05.get_rect()
guests_05.img.set_alpha(0)

guests_06 = imageload()
guests_06.put_img("project/source/guest/osu.png")
guests_06.change_size(300, 300)
guests_06.x = (screen_width / 2) - (guests_06.img.get_size()[0] / 2)
guests_06.y = 7
guests_06.get_rect()
guests_06.img.set_alpha(0)

guests_07 = imageload()
guests_07.put_img("project/source/guest/sech.png")
guests_07.change_size(300, 300)
guests_07.x = (screen_width / 2) - (guests_07.img.get_size()[0] / 2)
guests_07.y = 7
guests_07.get_rect()
guests_07.img.set_alpha(0)

guests_img = [guests_01.img, guests_02.img, guests_03.img, guests_04.img, guests_05.img, guests_06.img, guests_07.img]

#식재료(랜덤)
food_01 = imageload()
food_01.put_img("project/source/food/cheese.png")
food_01.change_size(150, 150)
food_01.x = (screen_width / 2) - (food_01.img.get_size()[0] / 2)
food_01.y = 0
food_01.get_rect()

food_02 = imageload()
food_02.put_img("project/source/food/patty.png")
food_02.change_size(150, 150)
food_02.x = (screen_width / 2) - (food_02.img.get_size()[0] / 2)
food_02.y = 0
food_02.get_rect()

food_03 = imageload()
food_03.put_img("project/source/food/chicken.png")
food_03.change_size(150, 150)
food_03.x = (screen_width / 2) - (food_03.img.get_size()[0] / 2)
food_03.y = 0
food_03.get_rect()

food_04 = imageload()
food_04.put_img("project/source/food/shirip.png")
food_04.change_size(150, 150)
food_04.x = (screen_width / 2) - (food_04.img.get_size()[0] / 2)
food_04.y = 0
food_04.get_rect()

# food_02 = imageload()
# food_02.put_img("project/source/food/patty.png")
# food_02.change_size(150, 150)
# food_02.x = (screen_width / 2) - (food_02.img.get_size()[0] / 2)
# food_02.y = 0
# food_02.get_rect()

food_06 = imageload()
food_06.put_img("project/source/food/lettuce.png")
food_06.change_size(150, 150)
food_06.x = (screen_width / 2) - (food_06.img.get_size()[0] / 2)
food_06.y = 0
food_06.get_rect()

food_07 = imageload()
food_07.put_img("project/source/food/tomato.png")
food_07.change_size(150, 150)
food_07.x = (screen_width / 2) - (food_07.img.get_size()[0] / 2)
food_07.y = 0
food_07.get_rect()

food_08 = imageload()
food_08.put_img("project/source/food/onion.png")
food_08.change_size(150, 150)
food_08.x = (screen_width / 2) - (food_08.img.get_size()[0] / 2)
food_08.y = 0
food_08.get_rect()

food_09 = imageload()
food_09.put_img("project/source/food/pickle.png")
food_09.change_size(150, 150)
food_09.x = (screen_width / 2) - (food_09.img.get_size()[0] / 2)
food_09.y = 0
food_09.get_rect()

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

menu_bar = imageload()
menu_bar.put_img("project/source/ui/menu_bar.png")
menu_bar.change_size(100, 480)
menu_bar.x = screen_width - menu_bar.img.get_size()[0]
menu_bar.y = 0

order_text = imageload()
order_text.put_img("project/source/ui/menu_bar.png")
order_text.change_size(520, 150)
order_text.x = 10
order_text.y = screen_height - 160

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
                    game_progress_state = 2
                if game_progress_state == 2:
                    okbt_press_state += 1
                    if okbt_press_state >= 2:
                        game_bg.show()
                        pygame.display.update()
                        game_progress_state = 3
                        guest_presence_or_absence = 1
                        order_text.show()
                        menu_bar.show()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_f:
                random_things = random.randint(1, 9)
            if event.key == pygame.K_e:
                guest_presence_or_absence = 1
                guest_all_alpha(0)
    
    if game_progress_state == 3:
        
    #     while passed_guest < satisfaction:
        order_guest = 0
        order_menu = 0
        random_things = 0
        press_key = 0

        choose_things = []


        order_guest = guests[random.randint(0, len(guests)-1)]
        if order_guest == normal_guest:
            order_menu = normal_guest[random.randint(0, len(normal_guest)-2)]
        elif order_guest == fat_guest:
            order_menu = fat_guest[random.randint(0, len(fat_guest)-2)]
        elif order_guest == weird_guest:
            order_menu = weird_guest[random.randint(0, len(weird_guest)-2)]

        while guest_presence_or_absence == 1:
            order_guest_img = guests_img[random.randint(0, len(guests_img)-1)]
            order_guest_img.set_alpha(255)
            for i in range(0, 7):
                print(guests_img[i].get_alpha())

            print("========")
            guest_presence_or_absence = 0

    

        # print("{0}버거 주세요".format(order_menu[2]))
        # print(order_menu[0])


    #     if order_guest[1] == "weird": 
    #         random_things = random.randint(11, 13)
    #     else:
    #         random_things = random.randint(1, 6)
    #     print(random_things)

    #     while press_key != "e":
    #         f 누르고 엔터 : 재료 바꾸기, e 누르고 엔터 : 음식 완성 , 엔터 : 재료 선택
    #         print("----------------------")
    #         # press_key = input("[ F : Change , Enter : Choose , E : complete ]")
    #         if press_key == "f":
    #             if order_guest[1] == "weird": 
    #                 random_things = random.randint(11, 13)
    #             else:
    #                 random_things = random.randint(1, 6)
    #             print(random_things)
    #             money -= 500
    #         elif press_key == "e":
    #             if order_menu[0] == choose_things:
    #                 print("perfect")
    #                 print("잘만드노 ㅋ")
    #                 money += order_menu[1]
    #             else:
    #                 choose_things.sort()
    #                 if choose_things == order_menu[0]:
    #                     print("complete")
    #                     print("야미")
    #                     money += order_menu[1]
    #                 else:
    #                     print("ㅈㄴ못만드네")
    #                     money -= 2000
    #                     satisfaction -= 1
    #         elif press_key != "e" or "f":
    #             if press_key == "":
    #                 choose_things.append(random_things)
    #             else:
    #                 continue
    #         print(choose_things)
    #         print(order_menu[0])
    #         print("남은돈 : {0}".format(money))

    #         print("----------------------")

    #     passed_guest += 1  

    #     if satisfaction > 10:
    #         satisfaction = 10

    #     if satisfaction <= 0:
    #         print("만족도가 너무 하락하여 알바를 고용하였습니다 (만족도 2 상승)")
    #         satisfaction = 2
    #         money - 10000

    #     if money < 0:
    #         if loan_state == 0:
    #             print("돈이 다 떨어져 빚을 졌습니다")
    #             loan_state = 1
    #     else:
    #         loan_state = 0

    
    # passed_guest = 0
    # passed_days += 1
    # print("----------------------")
    # print("하루가 지났다 | {0}일차 끝".format(passed_days))
    # print("남은돈 : {0}".format(money))
    # print("만족도 : {0}".format(satisfaction))
    # print("----------------------")


                


    


    if game_progress_state == 0:
        intro_bg.show()
        start_button.show()

        food_01.show()
        food_02.show()
        food_03.show()
        food_04.show()
        # food_05.show()
        food_06.show()
        food_07.show()
        food_08.show()
        food_09.show()
        food_all_alpha(0)

        guests_01.show()
        guests_02.show()
        guests_03.show()
        guests_04.show()
        guests_05.show()
        guests_06.show()
        guests_07.show()
        guest_all_alpha(0)
        # for i in range(0, 7):
        #     print(guests_img[i].get_alpha())
        # print("========")


    pygame.display.update()

pygame.quit()