# 중첩 for문
for i in range(3):
    for j in range(2):
        print(f'i ={i}, j= {j}')
print('_'*30)


for dan in range(2, 10):
    print('  ', dan,'단')
    for i in range(1,10):
        print(f'{dan} * {i} = {dan*i}')
    print()


# 구구단 가로 출력
'''
2*1=2   3*1=3   4*1=4   ... 9*1=9
2*2=4   3*2=6   4*2=8   ... 9*2=18
...
2*9=18  3*9=27  4*9=36  ... 9*9=81
'''

for i in range(1,10):
    for dan in range(2, 10):
        #1
        print('%d*%d=%2d'%(dan, i, dan*i), end= '  ')
        #2
        print(f'{dan}*{i}={dan*i:2d}', end='  ')
    print()

