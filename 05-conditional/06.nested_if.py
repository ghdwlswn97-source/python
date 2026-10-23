# 20세 이상 -> 성년
# 15세 ~ 18 -> 청소년
# 15세 미만 -> 어린이

#1
age = int(input('나이 입력 : '))
if age > 19:
    print('성년입니다.')
elif age >= 15:
    print('청소년입니다.')
else:
    print('어린이 입니다.')

#2
if age <= 19:
    if age > 15:
        print('청소년입니다.')
    else:
        print('어린이입니다.')
else:
    print('성년 입니다.')