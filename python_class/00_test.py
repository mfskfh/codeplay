class 참치선물세트:
    def __init__(self, 일반, 야채, 고추):
        self.일반 = 일반
        self.야채 = 야채
        self.고추 = 고추
    
    def 내용물보기(self, name):
        print(name)
        print("일반참치 : " + str(self.일반))
        print("야채참치 : " + str(self.야채))
        print("고추참치 : " + str(self.고추))
        
    # 일반 = 0
    # 야채 = 0
    # 고추 = 0

    # def 총합(self, 이름):
    #     내용물갯수 = self.일반 + self.야채 + self.고추
    #     print(이름 + str(내용물갯수))

    # def 출력(self):
    #     self.총합("담긴 참치 갯수 : ")

참치1호 = 참치선물세트()
참치1호.일반 = 5
참치1호.야채 = 3
참치1호.고추 = 2

# 참치갯수 = 참치1호.출력("담긴 참치 갯수 : ")

# print(참치갯수)

참치1호.출력()


참치3호세트 = 참치선물세트()

참치3호세트.일반 = 12
참치3호세트.야채 = 3
참치3호세트.고추 = 3

# print(참치3호세트.일반)

class Units:
    hp = 0
    damage = 0
    speed = 0

timo = Units()
timo.hp = 10
timo.damage = 100
timo.speed = 50

yasuo = Units()
yasuo.hp = 5
yasuo.damage = 1000
yasuo.speed = 100

# print("티모 - 체력 : {0} | 공격력 : {1} | 이속 : {2}".format(timo.hp, timo.damage, timo.speed))

