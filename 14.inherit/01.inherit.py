class CalcParent:
    def plus(self,x, y):
        print('부모클래스의 plus()')
        return x+y

    def minus(self, x, y):
        print('부모클래스의 minus()')
        return x-y

class CalcChild(CalcParent):        # CalcParent를 상복받음
    def multi(self, x, y):
        print('자식클래스의 multi()')
        return x*y

    def plus(self,x, y):
        # super().plus(x,y) 부모클래스의 plus호출
        print('부모의 plus',super().plus(x,y))
        print('자식클래스의 plus()')
        return (x+y)*2

cal1 = CalcChild()
print(cal1.minus(5,3))
print(cal1.plus(3,2))
print(cal1.multi(2,3))

cal2 = CalcParent()
print(cal2.plus(3,5))
# print(cal2.multi(2,3)) error 부모클래스에는 multi가 없음

