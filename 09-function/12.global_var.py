def fun1():
    a=19        # 지역변수 : 함수 안에서 사용 가능 
    print('fun1()의 a=', a)
    print('fun1()에서 전역변수 a =', globals()['a'])


# print(a)        # 출력 error

def fun2():
    print('fun2()의 a=', a)

a=20        # 전역변수 호출 전은 어느위치든 가능

fun1()
fun2()

def fun3():
    global b
    b=100
    print('fun3()의 b =', b)

def fun4():
    print('fun4()의 b=', b)

fun3()
fun4()

def clac_area(radius):
    global area 
    area = 3.14* radius**2
    return area

print(clac_area(5))
print(area)