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