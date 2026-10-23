'''
한 과일 가게의 현재 과일 재고 수량이 다음과 같이 딕셔너리에 저장되어 있다
inventory = {
        'apple: 15,
        'banana': 8,
        'orange': 20,
        'melon': 3
        }
문1. 가게에 포도('grape')가 12개 새로 들어왔다.추가하기
문2. 손님이 망고('mango')가 있는지 물어보았다. 망고가 있으면 재고 출력, 없으면 '재고가 없습니다.'출력 get()메서드 사용
문3. 오늘 마감 전 현재 가게에 남아있는 모든 과일의 이름과 재고 수량을 아래 보기와 같은 형식으로 한 줄씩 출력하는 코드를 작성(단 items() 메서드 사용)
        [출력보기]
        과일 : apple | 재고 : 15개
        과일 : banana | 재고 : 8개
'''
inventory = {
        'apple' : 15,
        'banana': 8,
        'orange': 20,
        'melon': 3
        }
# 문 1
inventory['grape'] = 12
print(inventory)

# 기존에 있는 key에 값 추가
inventory['apple'] = inventory['apple'] + 12
inventory['apple']+= 12
# 기존에 있는 key값인지 모를때 if문 활용
in_fr = 'apple'     # 새로추가하는 key 값을 변수로 만들어 활용
if in_fr in inventory:
    inventory[in_fr] += 12
else :
    inventory[in_fr] = 12
print(inventory)

# 문 2
if 'mango' in inventory:
    print('망고 재고 : ', inventory['mango'] )
else:
    print('재고가 없습니다.')
# get 메서드 활용
mango= inventory.get('mango',0)
print('망고 수량 :', mango)

# 문 3
for fruit, count in inventory.items():
    print(f'과일: {fruit} | 재고: {count}개')

