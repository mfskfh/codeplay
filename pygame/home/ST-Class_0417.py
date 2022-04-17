#클래스
class JSS:
    def __init__(self):
        self.name = input("이름:")
        self.age = input("나이:")
    def show(self):
        print("나의 이름은 {}, 나이는 {}세입니다.".format(self.name,self.age))

#JSS와 같은 클래스를 복사
class JJS2(JSS):
    pass

#클래스 상속(혹시를 위해 수정을 하지 않고새로 만들기)
class JSS3(JSS):
    def __init__(self):
        super().__init__() #JSS(super)에 있는 __init__함수를 가지고 온다
        self.gender = input("성별:")
    def show(self):
        print("나의 이름은 {}, 성별은 {}자, 나이는 {}세입니다.".format(self.name,self.gender,self.age))

a = JSS3()

a.show()