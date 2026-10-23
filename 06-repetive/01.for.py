for X in 'abcdefg' :
    print(X)
print('-'*30)

for i in [0, 6, 8, 3]:
    print(i)
print('-'*30)

num = [0, 6, 8, 3]
for i  in num:
    print(i)
print('-'*30)

'''
range(시작값, 종료값, step)
range(종료값) ->시작값 default=0, step default=1
range(시작값, 종료값) -> step default=1
'''

for X in range(5): # 0~4
    print(X)
print('-'*30)

for X in range(3, 10):
    print(X)
print('-'*30)

for X in range(1, 10, 3):
    print(X)

for X in range(1, 20, 2):
    print(X, end = ', ')    # 엔터 치지말고 ,로 교체
print('-'*30)

for X in range(1, 20, 2):   # 마지막 숫자에는 , 생략
    if X < 19:
        print(X, end =', ')
    else :
        print(X)