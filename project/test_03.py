# -*- coding: utf-8 -*-

import random
from data_01 import *

def percent (a):
    percent_value = random.randint(1, a)
    if 0 < percent_value <= a:
        return True
    else:
        return False

satisfaction = 10

passed_guest = 0  
order_guest = 0
order_menu = 0
random_things = 0
press_key = 0

choose_things = []

money = 10000

passed_days = 0
passed_guest = 0

while passed_days < 7:
    while passed_guest < satisfaction:
  
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
        
        print("----------------------")
        print("{0}버거 주세요".format(order_menu[2]))
        print(order_menu[0])

        if order_guest[1] == "weird": 
            random_things = random.randint(11, 13)
        else:
            random_things = random.randint(1, 6)
        print(random_things)

        while press_key != "e":
        #f 누르고 엔터 : 재료 바꾸기, e 누르고 엔터 : 음식 완성 , 엔터 : 재료 선택
            print("----------------------")
            press_key = input("[ F : Change , Enter : Choose , E : complete ]")
            if press_key == "f":
                if order_guest[1] == "weird": 
                    random_things = random.randint(11, 13)
                else:
                    random_things = random.randint(1, 6)
                print(random_things)
                money -= 500
            elif press_key == "e":
                if order_menu[0] == choose_things:
                    print("perfect")
                    print("잘만드노 ㅋ")
                    money += order_menu[1]
                else:
                    choose_things.sort()
                    if choose_things == order_menu[0]:
                        print("complete")
                        print("야미")
                        money += order_menu[1]
                    else:
                        print("ㅈㄴ못만드네")
                        money -= 2000
                        satisfaction -= 1
            elif press_key != "e" or "f":
                if press_key == "":
                    choose_things.append(random_things)
                else:
                    continue
            print(choose_things)
            print(order_menu[0])
            print("남은돈 : {0}".format(money))

            print("----------------------")

        passed_guest += 1  

        if satisfaction > 10:
            satisfaction = 10

        if satisfaction <= 0:
            print("만족도가 너무 하락하여 알바를 고용하였습니다 (만족도 2 상승)")
            satisfaction = 2
            money - 10000

        if money < 0:
            if loan_state == 0:
                print("돈이 다 떨어져 빚을 졌습니다")
                loan_state = 1
        else:
            loan_state = 0

    
    passed_guest = 0
    passed_days += 1
    print("----------------------")
    print("하루가 지났다 | {0}일차 끝".format(passed_days))
    print("남은돈 : {0}".format(money))
    print("만족도 : {0}".format(satisfaction))
    print("----------------------")