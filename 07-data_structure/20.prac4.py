'''
로또 프로그램 만들기
사용자로부터 몇회분을 살건지 물어보고
그 횟수만큼 번호를 랜덤으로 추출하여 출력하기
'''
# 1
import random
count = int(input('몇회분을 구매하시겠습니까? '))

for i in range(count):
    lotto_set = set()
    while len(lotto_set) < 6:
        num = random.randint(1, 45)
        lotto_set.add(num)

    lotto_list = sorted(lotto_set)
    print(f'{i+1}회차 : {lotto_list}')


# 2
import random

count = int(input('실행 횟수 :'))

for i in range(count):
    lotto=set()
    while len(lotto) <6:
        num = random.randint(1, 45)
        lotto.add(num)
    print(f'{i+1}회차 : {lotto}')

