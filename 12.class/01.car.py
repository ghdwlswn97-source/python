'''
* 파일명은 소문자로 시작, 클래스명은 대문자로 시작

* 클래스 선언
    class 클래스명: 
        메서드 생성
        # pass -> 빈상태로 만들 때 사용(임시 점유용 키워드)

* 매개변수 self
    자기자신의 객체를 의미
    클래스 안에서 함수를 호출할 때

    이름이 반드시 self가 아니어도 되지만 보통 self를 씀

'''
class Car:
    def set1(self):
        self.model='sm7'
        self.color='blue'
        self.speed=10

    def speedUp(self):
        self.speed=20

    def output(self):
        print('모델 :', self.model)
        print('색상 :', self.color)
        print('속도 :', self.speed)

myCar = Car()
myCar.set1()        # 호출할 때 변수가 생성 되면서 초기화가 됨 생략하면 error
myCar.output()
print('-'*30)

myCar.speedUp()
myCar.output()

print(myCar.model)
print(myCar.color)
print(myCar.speed)
