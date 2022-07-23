# class 참치선물세트:
#     def __init__(self, 일반, 야채, 고추):
#         self.일반 = 일반
#         self.야채 = 야채
#         self.고추 = 고추
    
#     def 내용물보기(self, name):
#         print(name)
#         print("일반참치 : " + str(self.일반))
#         print("야채참치 : " + str(self.야채))
#         print("고추참치 : " + str(self.고추))

# class 특별선물세트(참치선물세트):
#     def __init__(self, 일반, 스팸, 올리브유):
#         super().__init__(일반, 0, 0)
#         self.스팸 = 스팸
#         self.올리브유 = 올리브유

#     def 내용물보기(self, name):
#         super().내용물보기(name)
#         print("스펨 : " + str(self.스팸))
#         print("올리브유 : " + str(self.올리브유))

# 특별01 = 특별선물세트(6, 3, 2)
# 특별01.내용물보기("특별세트 1호")

    # 일반 = 0
    # 야채 = 0
    # 고추 = 0

    # def 총합(self, 이름):
    #     내용물갯수 = self.일반 + self.야채 + self.고추
    #     print(이름 + str(내용물갯수))

    # def 출력(self):
    #     self.총합("담긴 참치 갯수 : ")

# 참치1호 = 참치선물세트()
# 참치1호.일반 = 5
# 참치1호.야채 = 3
# 참치1호.고추 = 2

# 참치갯수 = 참치1호.출력("담긴 참치 갯수 : ")

# print(참치갯수)

# 참치1호.출력()


# 참치3호세트 = 참치선물세트()

# 참치3호세트.일반 = 12
# 참치3호세트.야채 = 3
# 참치3호세트.고추 = 3

# print(참치3호세트.일반)

# class Units:
#     hp = 0
#     damage = 0
#     speed = 0

# timo = Units()
# timo.hp = 10
# timo.damage = 100
# timo.speed = 50

# yasuo = Units()
# yasuo.hp = 5
# yasuo.damage = 1000
# yasuo.speed = 100

# print("티모 - 체력 : {0} | 공격력 : {1} | 이속 : {2}".format(timo.hp, timo.damage, timo.speed))

class 캐릭터():
    def __init__(self, 체력, 공격력, 이동속도):
        self.체력 = 체력
        self.공격력 = 공격력
        self.이동속도 = 이동속도
    
    def 상태보기(self, name):
        print(name)
        print("체력 : {0}".format(self.체력))
        print("공격력 : {0}".format(self.공격력))
        print("이동속도 : {0}".format(self.이동속도))

class 챔피언(캐릭터):
    def __init__(self, 체력, 공격력, 이동속도, q, w, e, r):
        super().__init__(체력, 공격력, 이동속도)
        self.q = q
        self.w = w
        self.e = e
        self.r = r

    def 상태보기(self, name):
        super().상태보기(name)
        print("q : {0}".format(self.q))
        print("w : {0}".format(self.w))
        print("e : {0}".format(self.e))
        print("r : {0}".format(self.r))
        
class 정글몹(캐릭터):
    def __init__(self, 체력, 공격력, 이동속도, 개체수):
        super().__init__(체력, 공격력, 이동속도)
        self.개체수 = 개체수

    def 상태보기(self, name):
        super().상태보기(name)
        print("개체수 : {0}".format(self.개체수))

class 구조물(캐릭터):
    def __init__(self, 체력, 공격력, 시아):
        super().__init__(체력, 공격력, 0)
        self.시아 = 시아

    def 상태보기(self, name):
        super().상태보기(name)
        print("시아 : {0}".format(self.시아))

# 미니언01 = 캐릭터(100, 5 ,20)
# 미니언01.상태보기("미니언 1번의 상태")

# print("----------")

# 야스오 = 챔피언(500, 25, 100, "강철폭풍", "바람 장막", "질풍검", "최후의 숨결")
# 야스오.상태보기("야스오의 상태보기")

# print("----------")

# 늑대 = 정글몹(250, 50, 50, 3)
# 늑대.상태보기("늑대의 상태보기")

# print("----------")

# 포탑 = 구조물(2000, 100, 100)
# 포탑.상태보기("포탑의 상태보기")

# print("----------")

# 와드 = 구조물(4, 0, 50)
# 와드.상태보기("와드의 상태보기")

texts = "택스트"
numbers = 1243
lists = []
tuple = ()

print(type(texts))
print(type(numbers))
print(type(lists))
print(type(tuple))