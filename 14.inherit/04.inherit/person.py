'''
02.inherti
    person.py
    programmer.py   (Person 상속)
    main.py
'''
class Person:
    def __init__(self, name, age, job=None):
        self.name =name
        self.__age = age
        self.job = job

    def hello(self):
        print(f"Hello, I'm {self.name}")

    def update_age(self, age):
        if age < 0:
            print('나이는 음수일 수 없습니다.')
        else : 
            self.__age =age
            print(f'현재 나이는 {self.__age}세')

    def getAge(self):
        return self.__age
    

# 잘 작동하는지 확인
if __name__== '__main__':
    p1 = Person('황미미', 27)
    p1.hello()
    p1.update_age(-3)
    p1.update_age(28)

    p1.__age = -7     # p1.겍체에 새로운 인스턴스 변수 생성
    print(f'나이는 {p1.__age}세')
    print(p1.getAge)  # 기존 객체에 들어있는 age값

    __age= -8       # 현 스택에서만 사용하는 변수
    print(__age)
    print(p1.__age)
    print(p1.getAge)