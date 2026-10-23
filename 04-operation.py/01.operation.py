# 산술연산자
num1 = int(input('정수 입력 : '))
num2 = int(input('정수 입력 : '))

r1 = num1 + num2
print(f'{num1}+ {num2} ={r1}')

r2 = num1 - num2
print(f'{num1} - {num2} = {r2}')

r3 = num1 * num2
print(f'{num1} * {num2} = {r3}')

r4 = num1/num2
print(f'{num1} / {num2} + {r4}')    # JAVA는 정수형으로 몫 출력. python은 실수형으로 몫이 출력된다

r5 = num1%num2  # 나머지
print(f'{num1}을 {num2}로 나눈 나머지 = {r5}')

r6 = num1 // num2 # 몫
print(f'{num1}을 {num2}로 나눈 몫 = {r6} ')

r7 = num1 **3 # 지수 연산자
print(f'{num1}의 {num2}승 = {r7}')

# 파이썬은 실수의 나머지도 구함
print(7.7 % 2.15)
