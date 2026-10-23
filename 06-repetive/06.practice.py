# 문 : 2개의 숫자를 입력받아 합계 구하기. 무한반복
#       사용자가 첫 번째 값에 0을 넣으면 종료



while True :
    num1 = int(input('첫 번째 숫자를 입력하시오 :'))
    if num1 == 0:
        break

    num2 = int(input('두 번째 숫자를 입력하시오 :'))
    
    print(f'2개의 숫자의 합 : {num1}+{num2}={num1+num2}\n')
print('계산 종료')