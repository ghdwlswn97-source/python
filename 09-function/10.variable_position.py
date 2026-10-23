# 가변 위치 인자 : 매개변수의 개수가 정해져 있지 않을 때 사용
# *args : 튜플이 전달되고 저장됨(변경 불가)

def total(*args):
    print(type(args))
    sum = 0
    for x in args:
        sum += x
    return sum
print(total(1, 3))
print(total(3,4,56,34))     # 여러개도 가능
print(total())      # 입력값 없으면 0출력
print()

# 매개변수가 여러개일 때   *args 맨뒤 입력
def add_mul(op, *args):
    if op == 'add':
        result=0
        for i in args:
            result += i
    elif op == 'mul':
        result = 1
        for i in args:
            result *= i
    return result
print(add_mul('add', 1, 2, 3, 4, 5))
print(add_mul('mul', 3,5))

# * args가 중간에 올때
def calc_sum(name, *args,academy):
    print(f'Name:{name}, Academy : {academy}')
    sum =0
    for x in args:
        sum += x
    return sum
print('합계 : ', calc_sum('최상급', 1,2,3,4, academy='더조은')) # *args의 끝을 나타내기 위해 academy='더조은'로 입력