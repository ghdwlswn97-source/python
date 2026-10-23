class Car:
    def __init__(self, speed=0, color='black', model='E-class'):
        self.speed = speed
        self.color = color
        self.model = model

    def output(self):
        print('속도 :', self.speed)
        print('색상 :', self.color)
        print('모델 :', self.model)

myCar = Car()
myCar.output()
print('-'*30)

myCar1 = Car(40)
myCar1.output()
print('-'*30)

myCar2 = Car(model='F-class')
myCar2.output()
print('-'*30)

myCar3 = Car(10, 'white', 'K7')
myCar3.output()
print('-'*30)

myCar3.__init__(50, 'yellow', 'K5')
myCar3.output()