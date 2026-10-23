# 무한반복으로 구구단 중 출력할 단수를 입력받아 출력
# 출력 후 구구단을 계속 할 것인지 확인 'y'입력시반복 

while True:
    dan = int(input('출력할 단수를 입력하세요 : '))
    for i in range(1, 10):
        print(f'{dan}*{i}={dan*i}')

    choose = input('계속하려면 "y" 입력 : ')
    if choose == 'Y' or choose == 'y':
    # == if choose.lower() == 'y': # 소문자로 변환 lower() 대문자로 변환 upper()
        continue
    else:
        print('프로그램 종료')
        break

