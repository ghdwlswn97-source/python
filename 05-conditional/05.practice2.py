# 문 : 점수를 입력받아 학점 출력
#   101점 이상, 음수 입력시 잘못 넣었다고 해야 함

jumsu = int(input('점수를 입력하세요 :'))

# 방법 1
if jumsu >= 90 and jumsu <=100:
    print('A학점')
elif jumsu >=80:
    print('B학점')
elif jumsu >=70:
    print('C학점')
elif jumsu >=60:
    print('D학점')
elif jumsu >=0:
    print('F학점')
else:
    print('잘못 입력했습니다.')

# 방법 2
if jumsu > 0 or jumsu < 100:
    if jumsu >= 90:
     print('A학점')
    if jumsu >=80:
     print('B학점')
    if jumsu >=70:
     print('C학점')
    if jumsu >=60:
     print('D학점')
    if jumsu >=0:
     print('F학점')
else:
    print('잘못 입력했습니다.')