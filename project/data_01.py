bulgogi = [[7, 8, 3], 3500, "bulgogi", "불고기버거"]
cheese = [[7, 8, 2, 3], 5000, "cheese", "치즈버거"]
chicken = [[7, 8, 4], "chicken", "치킨버거"]
shrimp = [[7, 8, 5], "shrimp", "새우버거"]

double = [[7, 2, 3, 7, 2, 3, 10], 7600, "double", "더블버거"]
chibeef = [[7, 4, 3, 9, 10], 6500, "chibeef", "치킨불고기버거"]
allin = [[2, 3, 4, 5, 6, 7, 8, 9, 10], 12000, "allin", "올인버거"]

foot = [[11, 12, 13], 4500, "foot"]

normal_guest = [bulgogi, cheese, chicken, shrimp, "normal"]
fat_guest = [double, chibeef, allin, "fat"]
weird_guest = [foot, "weird"]

guests = [normal_guest, fat_guest, weird_guest]
burger = [bulgogi, cheese, double, allin, foot]
