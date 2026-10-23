class Car:
    def __init__(self, speed=0, color='black', model='E-class'):
        self.speed = speed
        self.color = color
        self.model = model

    def output(self):
        print('속도 :', self.speed)
        print('색상 :', self.color)
        print('모델 :', self.model)

    def __str__(self):
        result = f'속도 : {str(self.speed)}, 색상 : {self.color}'
        return result

myCar = Car()
myCar.output()
print('-'*30)

print(myCar)
print(myCar.__str__())