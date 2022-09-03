# -*- conding: utf-8 -*-

import random

money = 10000

guests = ["normal", "fat"]
guest_number = 0

menus = [["bulgogi", "cheese"],["double","chicken_beef"]]
menu_numbers = [[[1, 2, 3], [4, 5, 6]], [[1, 2 ,3 ,4], [3, 4, 5, 6]]]
menu_number = 0

visiting_guests = guests[random.randint(0,(len(guests)-1))]

if visiting_guests == guests[0]:
    order = menus[0][random.randint(0,(len(menus)-1))]
    # print(order)
    if order == menus[0][0]:
        menu_number = menu_numbers[0][0]
    elif order == menus[0][1]:
        menu_number = menu_numbers[0][1]
elif visiting_guests == guests[1]:
    order = menus[1][random.randint(0,(len(menus)-1))]
    # print(order)
    if order == menus[1][0]:
        menu_number = menu_numbers[1][0]
    elif order == menus[1][1]:
        menu_number = menu_numbers[1][1]

print(menu_number)

choose_things = []

press_key = 0   
