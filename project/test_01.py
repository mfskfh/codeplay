# -*- conding: utf-8 -*-

import random

menus = ["bulgogi", "cheese"]
menu_numbers = [[1, 2, 3], [4, 5, 6]]
menu_number = 0

#주문(영어)
order = menus[random.randint(0,(len(menus)-1))]

#주문(숫자)
if order == "bulgogi":
    menu_number = menu_numbers[0]
elif order == "cheese":
    menu_number = menu_numbers[1]

print(menu_number)

#고른 재료
choose_things = []

#누른키
press_key = 0

#랜덤재료
random_things = random.randint(1, 6)
print(random_things)
print("{0}버거를 가져와라 ㅋ".format(order))
while press_key != "e":
    #f 누르고 엔터 : 재료 바꾸기, e 누르고 엔터 : 음식 완성 , 엔터 : 재료 선택
    press_key = input("[ F : Change , Enter : Choose , E : complete ]")
    if press_key == "f":
        random_things = random.randint(1, 6)
        print(random_things)
    elif press_key == "e":
        choose_things.sort()
        random_things = print(choose_things)
        if choose_things == menu_number:
            print("complete")
        else:
            print("z")
    elif press_key != "e" or "f":
        if press_key == "":
            choose_things.append(random_things)
            random_things = random.randint(1, 6)
            print(random_things)
        else:
            continue
    print(choose_things)