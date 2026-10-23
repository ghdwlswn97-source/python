# 사용자로부터 입력받기
# name = input('이름을 입력하세요 : ')
# print(name+'님 환영합니다')

# input() 함수의 결과는 문자열로 들어옴
# kor = input('국어점수를 입력하세요 : ')
# com = input('컴퓨터점수를 입력하세요 : ')

# int형 변환의 우선순위
# kor = input('국어점수를 입력하세요 : ')
# com = input('컴퓨터점수를 입력하세요 : ')
# print(int(kor)+int(com))  문자열+문자열 후에 int 변환  # print(int(kor +com))     int변환 후 더하기      
# print('%s + %s = %d' %(kor, com,int(kor)+int(com)))

#int형으로 변환
kor = int(input('국어점수를 입력하세요 : '))
com = int(input('컴퓨터점수를 입력하세요 : '))
print(kor+com)
print('%d + %d = %d' %(kor, com, kor+com))
print('%s + %s = %s' %(kor, com, kor+com))  # 보여줄때만 string으로
print(f'{kor}+ {com} = {kor+com}')
