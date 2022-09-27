bulgogi = [[6, 8, 2], 3500, "bulgogi", "불고기버거", [2, 6, 8]]
cheese = [[6, 7, 1, 2], 5000, "cheese", "치즈버거", [1, 2, 6, 7]]
chicken = [[6, 8, 3], 3500, "chicken", "치킨버거", [3, 6, 8]]
vegan = [[6, 7, 5], 3500, "vegan", "비건버거", [5, 6, 7]]
shrimp = [[6, 8, 4], 3500, "shrimp", "새우버거", [4, 6, 8]]

double = [[6, 1, 2, 6, 1, 2, 9], 7600, "double", "더블버거", [1, 1, 2, 2, 6, 6, 9]]
chibeef = [[6, 3, 2, 8, 9], 6500, "chibeef", "치킨불고기버거", [2, 3, 6, 8, 9]]
allin = [[1, 2, 3, 4, 5, 6, 7, 8, 9], 12000, "allin", "올인버거", [1, 2, 3, 4, 5, 6, 7, 8, 9]]

normal_guest = [bulgogi, cheese, chicken, vegan, shrimp, "normal"]
fat_guest = [double, chibeef, allin, "fat"]

guests = [normal_guest, fat_guest]
burger = [bulgogi, cheese, double, allin]
