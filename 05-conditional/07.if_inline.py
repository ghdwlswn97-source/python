# 삼항 연산식
'''
if num1 == 2:
    print('num1은 2입니다.')
else: 
print('num1은 2가 아닙니다.')
'''

# if일때 내용 + if+ else  + else 내용
num1 = 2
print('2입니다.')if num1 == 2 else print('2가 아닙니다.')

print('2입니다.' if num1 == 2 else '2가 아닙니다.')

# 합격, 불합격
score = 50

# 일반 조건문
if score >= 60:
    result = '합격'
else :
    result = "불합격"

# 삼항연산자    바로출력
print('합격' if score >=60 else '불합격')

# 삼항연산자로 변수에 저장 후 출력
result = '합격' if score >= 60 else '불합격'
print(result)

# 두수 중 큰수 찾기
num2 =13
num3 =5

max_num = num2 if num2 > num3 else num3
print(f'큰숫자는 {max_num} 입니다.')
print(f'{num2}과 {num3}중 큰숫자는 {max_num} 입니다.')

# 회문 : 왼쪽에서 읽은 것과 오른쪽으로 읽었을 때 같은 문자열
str = 'abcdcbad'

# #1
# if str == str[::-1] :
#     print(f'{str} : 회문')
# else :
#     print(f'{str} : 회문 아님')

# # 2
# print(str, ': 회문' if str == str[::-1] else ': 회문 아님')

#3
print(f"{str} : {"회문" if str == str[::-1] else "회문 아님"}")