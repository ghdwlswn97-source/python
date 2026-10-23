'''
문 1. 카페 주문
메뉴와 사이즈 2개를입력받음
만약 사이즈가 입력이 안되면 무조건 small사이즈임

문 2. 택배 배송정보
받는사람, 주소, 전화번호를 입력받음
순서와 상관없이 받아서 출력

문 3. 친구들과 식당에 가서 각자 낸 금액의 합계 구하기(tuple)
친구들이 갈 때마다 인원이 달라짐

문 4. 회원가입 정보를 입력받기(dict)
사람마다 입력하는 정보의 개수가 다를 수 있음
'''
# 문 1
def cafe(name, size='small'):
    print(name, size)

cafe('라떼')

# 문 2
def delivery(name, address, phone):
    print('받는사람 :', name)
    print('주소 :', address)
    print('전화번호 :', phone)

delivery(phone='010-9454-4515', name='김철수', address='강남')

# def box(**kwargs):
#     for key, value in kwargs.items():
#         print(key,':', value)

# box(name='홍길동', ad='서울', phone=1234)

# 문 3
def total(*args):
    sum =0
    for i in args:
        sum += i
    return total

print(total(4000, 49880))

# 문 4
def info(**kwargs):
    for key, value in kwargs.items():
        print(key, ':', value)

info_list={'name':'홍진주', 'age' : 30}

info(**info_list)



    

