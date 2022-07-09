# -*- coding: utf-8 -*-

import random

Num = int(input("아무 양수나 넣으시오."))

if Num < 0:
    Num *= -1

if Num == 0:
    Num = random.randint(1, 100)
    print(Num)


#숫자가 짝수면 나누기 2, 숫자가 홀수면 곱하기 3 더하기 1
while Num != 1:
    if Num % 2 == 0:
        Num /= 2
        print(int(Num))
        if Num == 1:
            continue
    elif Num % 2 != 0:
        Num = (Num * 3) + 1
        print(int(Num))
        if Num == 1:
            continue

print("이런 ㅠ")