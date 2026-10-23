'''
# 함수 : 클래스 바깥쪽에 독립적으로 존재, 이름만으로 바로호출할 수 있음
# 메서드 : 클래스 내부에 정의되어 있고,객체를 통해서 호출하는 함수

def 함수명(매개변수들):
    실행문
    return
'''

# 매개변수가 없고, 반환값이 없는 함수
def address():
    print('서울특별시 강남구')
    print('삼오빌딩 704호')

address()
print('-'*40)

def add():
    a = 3+8
    print(a)

add()       # 리턴값이 없어서 print(add()) 하면 None나옴

# 매개변수가 없고 반환값이있는 함수
def add2():
    a=3+8
    return a        # add2()가 11을 받음

print(add2())       # 11
result = add2()
print(result)

print('-'*40)

# 매개변수가 있는 함수
def multi(x, y):
    result = x*y
    print(f'{x}*{y}={result}')

multi(3, 7)

def multi2(x, y):
    result=x*y
    return result

print(multi2(4, 8))

def star(n):
    for x in range(n):
        print('*', end='')
    print()

star(5)
star(10)

