'''
문 1 : 매개변수로 2개의 숫자와 연산자를 입력받아 출력
(num1, num2, op)

문 2 : 국어, 영어 점수를 사용자로부터 입력받아 함수로 평균을 입력받아 평균의 학점을 return

문 3 : 로또를 함수로

문 4 : 입력한 비밀번호가 규칙에 맞으면 생성되고 규칙에 맞지않으면 다시 생성하도록 메시지를 출력하는 프로그램을 작성
    1. 8글자 이상
    2. 문자 및 숫자로만 생성해야 하며 기호는 불가능

    새로운 비밀번호를 입력하세요 : abcd
    오류. 비밀번호가 규칙에 맞지 않습니다

    새로운 비밀번호를 입력하세요 : abcd1234$$$
    오류. 비밀번호가 규칙에 맞지 않습니다

    새로운 비밀번호를 입력하세요 : 1234abcd
    비밀번호가 생성 되었습니다
'''

#문 1
def math (num1, op, num2) :

    if op == '+':
        print(f'{num1}+{num2}={num1+num2}')
    elif op == '-':
        print(f'{num1}-{num2}={num1-num2}')
    elif op == '*':
        print(f'{num1}*{num2}={num1*num2}')
    elif op == '/':
        print(f'{num1}/{num2}={num1/num2}')

#     a = int(input('첫번째 숫자'))
#     op=input('연산자를 입력하세요')
#     b = int(input('두번째 숫자'))
# print(math(a, op, b))


# 문 2
# kor = int(input('국어점수 :'))
# eng = int(input('영어점수 :'))
# avg= (kor + eng) / 2

# def grade(avg):
#     if avg >=90: return 'A'
#     elif avg >=80: return 'B'
#     elif avg >=70: return 'C'
#     elif avg >=60: return 'D'
#     else: return 'F'

# # 문 2 내답
# def avg(x,y):
#     result = (x+y)/2
#     return result
# print(avg(90,87))

# 문 3
import random

def lotto():
    lotto_set = set()
    while len(lotto_set) < 6:
            num = random.randint(1, 45)
            lotto_set.add(num)
    
    lotto_list = sorted(lotto_set)
    print(f'오늘의 행운번호 : ', lotto_list)

lotto()

# 문 3 내답    
# import random
# def lotto():
#     lotto=set()
#     while len(lotto) < 6:
#         num=random.randint(1,45)
#         lotto.append(num)

# 문 4
def checkPwd(pwd):
    if len(pwd)<8:
        return False
    if pwd.isalnum():
        return True
    else:
        return False

    # if len(pwd)>=8 and pwd.isalnum():
    #     return True
    # else:
    #     return False

password = input('비밀번호 입력: ')
if checkPwd(password):
    print('비밀번호가 생성되었습니다')
else:
    print('비밀번호 규칙에 맞지 않습니다.')
    



