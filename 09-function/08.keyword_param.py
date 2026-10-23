# 키워드 인자
def display_info(academy, name, classroom):
    print(f'Academy : {academy}, Name : {name}, ClassRoom : {classroom}')

display_info('더조은', '이승우', '704호')

def display_info2(name, classroom, academy='더조은'):       # 디폴트 값이 들어가면 맨뒤에 입력
    print(f'Name : {name}, ClassRoom : {classroom}, Academy : {academy}')
# 입력 순서대로 출력
display_info2('한수철', '303호')
# 입력 순서와 무관하게 나오게 하려면
display_info2(classroom='703호', academy='한샘', name = '박미화')
