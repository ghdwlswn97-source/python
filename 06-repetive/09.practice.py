# import random
# x = random.random()
# i = random.randint(1, 3)    # end 포함  1, 2, 3중에 랜덤으로 숫자 하나
# print(x)
# print(i)

# 문 : 주사위를 3개를 동시에 던져서 동일한 숫자가 나오면 탈출
# 출력 : 주사위에 나온 숫자와 횟수

import random

count = 0

while True : 
    count += 1
    x = random.randint(1, 6)
    y = random.randint(1, 6)
    z = random.randint(1, 6)   
    if x == y == z:
        break
print(f'{x}, {y}, {z} 횟수 : {count}')
        


# 문 : 주사위의 숫자 맞추기. 몇회만에 맞췄는지


count = 0
while True :
    count += 1
    print('게임', count, '회')
    X = random.randint(1, 6)
    num = int(input('주사위 숫자를 입력하세요 :'))
    if X == num:
        print('맞췄습니다', count, '회만에 맞췄습니다.')
        break
    else :
        print('안타깝네요', X, '입니다. 다시 합니다.')
        continue