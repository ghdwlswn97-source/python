'''
문 :사용자한테 전화번호를 입력받아
    하이픈을 제거하고 오직 숫자만 구성되어 있는지 확인
    숫자 중 '0'의 갯수 세기
'''
phone=input('전화번호 입력:')
number= phone.replace('-','')

if number.isdigit():
    print('숫자로만 구성되어있는가? :')
    print(f'0의 개수 : {number.count('0')}')
else:
    print('잘못입력했습니다.')




phone = input('전화번호를 입력하세요 :')
#하이픈 제거
number = phone.replace('-','')
isNum =number.isdigit()

if isNum :
    zero_count = number.count('0')
    print('0의갯수: ', zero_count)
else:
    print('잘못입력했습니다')

print('숫자로만 구성되어 있는가?', phone.isdigit())
print('0은 몇개인가? :', phone.count('0'))