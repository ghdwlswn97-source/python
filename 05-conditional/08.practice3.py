# 사용자로부터 두 수를 입력 받고 연산자도 입력받음
# 연산 결과를 출력하기
# +, -, *, /, //, %,  **

# 내 답 
num1 = int(input('첫 번째 수를 입력하세요 :'))
num2 = int(input('두 번째 수를 입력하세요 :'))
result = input('연산자를 입력하세요 :')

if result == '+' :
    print(num1+num2)
if result =='-':
    print(num1-num2)
if result =='*':
    print(num1*num2)
if result =='/':
    print(num1/num2)
if result =='//':
    print(num1//num2)
if result =='%':
    print(num1%num2)
if result =='**':
    print(num1**num2)

# 답
num1 = int(input('첫 번째 수를 입력하세요 :'))
num2 = int(input('두 번째 수를 입력하세요 :'))
op = input('연산자를 입력하세요 :')

result = 0

if op == '+' :
    result = num1+num2
if op =='-':
    result = num1-num2
if op =='*':
    result = num1*num2
if op =='/':
    result = num1/num2
if op =='//':
    result = num1//num2
if op =='%':
    result = num1%num2
if op =='**':
    result = num1*num2

print(num1, op, num2, '=', result)

    

# 숫자를 입력받아
# 양수이면서 홀수/짝수 인지
# 음수이면서 홀수/짝수 인지

num1 = int(input('첫 번째 숫자를 입력하세요 :'))
num2 = int(input('두 번째 숫자를 입력하세요 :'))

# 내답
if num1>0 and num1%2==0:
    print('양수 짝수 입니다.')
elif num1>0 and num1%2!=0:
    print('양수 홀수 입니다.')
elif num1<0 and num1 %2 == 0:
    print('음수 짝수 입니다.')
elif num1 <0 and num1 %2 != 0:
    print('음수 홀수 입니다.')

#1
if num1 >0:
    print('양수 이면서', end=' ')
    if num1 %2 ==0:
        print('짝수')
    else:
        print('홀수')
elif num1 < 0:
    print('음수 이면서', end=' ')
    if num1 %2 ==0:
        print('짝수')
    else:
        print('홀수')
else :
    print('0입니다.')

#2
if num1 == 0:
    print('0입니다.')
else:
    if num1 > 0 :
        print('양수 입니다.')
    else :
        print('음수 입니다.')
    if num1 %2 == 0:
        print('짝수 입니다.')
    else:
        print('홀수 입니다.')

#3
if num1 == 0:
    print('0입니다.')
else:
    sign = '양수' if num1 >0 else '음수'
    parity = '짝수' if num1 %2 ==0 else '홀수'
    print(sign, '입니다.')
    print(parity, '입니다.')