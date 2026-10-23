'''
문
파운드(lb)와 킬로그램(kg)을 상호 변환하는 프로그램 만들기

kg = pound * 0.453592
pound = kg * 2.204623
'''

pound = int(input('파운드 입력 : '))
kg = pound * 0.453592
print(f'{pound} 파운드는 {kg:.2f}kg 입니다')

kg = int(input('kg 입력 : '))
pound = kg * 2.204623
print(f'{kg}kg은 {pound:.2f}파운드 입니다')

# 내 답
pound = input('파운드 입력')
kg = input('킬로그램 입력')
kg = pound * 0.453592
pound= kg * 2.204623