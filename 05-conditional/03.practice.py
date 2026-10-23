# 문 : 정수를 입력받아 짝수인지 홀수인지 판별
num = int(input('정수를 입력하세요 : '))
if num % 2 == 0:
    print('짝수입니다.')
else:
    print('홀수입니다.')

# 문 : 정수 2개를 입력받아 큰값과 작은값을 출력
num1 = int(input('정수1을 입력하세요 : '))
num2 = int(input('정수2를 입력하세요 : '))

if num1 > num2:
    print(f'큰값 : {num1}, 작은값 : {num2}')
else:
    print(f'큰값 : {num2}, 작은값 : {num1}')

# 자리바꾸기
if num1 < num2:
    num1, num2 = num2, num1
print(f'큰값 : {num1}, 작은값 : {num2}')