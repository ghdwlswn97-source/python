# Comprehension
# 특히 리스트에서 많이 사용 -> list comprehension 이라고 불림
# for문이나 if문을 한줄에 넣는다

result =[0 for i in range(100)] # 0 백개인 리스트 만들기  [0, 0, 0, 0, ... 100개]
print(result)

result = [10 for x in range(100)]   # 10 백개
print(result)

result = [i+1 for i in range(100)]  # 1부터 100까지
print(result)

result = ['더조은' for i in range(100)]
print(result)

data = [3, 5, 7, 9]
result = [x**2 for x in data]
print(result)   #[9, 25, 49, 81]

# 사용자가 넣은 수로 리스트 만들기
numList = [int(input('숫자입력 : ')) for x in range(5)]
print(numList)
print('합계 :', sum(numList))

# if와 for문이 함께 들어있을 때는 무조건 for문 부터
print('_'*50)

result=[]
for num in range(1, 20):
    if num % 2 == 0:
        result.append(num*3)

result =  [num*3 for  num in range(1, 20) if num % 2 == 0]
print(result)

# for, if, else는 if, else, for 순으로 작성
result=[]
for num in range(1, 10):
    if num % 2 == 0 :
        result.append(num)
    else:
        result.append(0)

result = [num if num % 2 == 0 else 0 for num in range(1, 10)]
print(result)

# 1~5를 홀수, 짝수로 표현
result = ['짝수' if num % 2 == 0 else '홀수' for num in range(1, 6)]
print(result)

# for문이 중첩으로 들어갈 때
result = []
for x in [1, 2, 3]:
    for y in [10, 20]:
        result.append((x,y))

result = [(x, y) for x in [1, 2, 3] for y in [10, 20]]
print(result)

result = []
for x in range(1, 4):
    for y in range(1, 4):
        if (x+y) % 2 == 0:
            result.append((x,y))
print(result)

result = [(x,y) for x in range(1, 4) for y in range(1, 4) if (x+y )% 2 == 0]
print(result)

result = []
for x in range(1, 4):
    for y in range(1, 4):
        if (x+y) % 2 == 0:
            result.append((x,y))
        else:
            result.append((0,0))
print(result)

result = [(x, y) if(x+y) % 2 ==0 else(0,0) for x in range(1,4) for y in range(1,4)]
print(result)

# unpacking
list1 = [(1,11),(2,21),(3,31)]
for (first, last) in list1:
    print(first+last)

result = [first+last for (first, last) in list1]
print(result)

# enumerate() : 인덱스 번호와 데이터를 tuple의 형태로 반환
t = [1, 4, 5, 7,41, 50]
for p in enumerate(t):
    print(p)

for i, v in enumerate(t):
    print(f'index : {i}, value : {v}')

# zip() : 리스트 두개를 동일한 위치값으로 묶어서 관리. tuple로 반환
# 길이가다르면 짧은 길이로묶음
list1 = [10,20,30]
list2 = [100, 200,300]

for z in zip(list1, list2):
    print(z)

for a,b in zip(list1,list2):
    print(a+b)

for a,b in zip(list1,list2):
    print(a*b)
