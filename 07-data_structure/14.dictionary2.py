dic1 = {'a':1, 'b':3.141592,'c':'hello', 'd':'파이썬'}

# key가 없을 경우 대비
if 'e' in dic1:
    print('키가 존재함 :', dic1['c'])
else:
    dic1['e'] = 'bye'
print(dic1)

# key만 확인
result = dic1.keys()
print(result)
print(type(result))
print('_'*30)

# 값만 확인
print(dic1.values())
print('_'*30)

# items() : 딕셔너리의 키와 값을 쌍으로묶어서 가져오는 함수
print(dic1.items())
print('_'*30)

for key in dic1.keys():
    print(key)
print('_'*30)

for key, value in dic1.items():
    print(key, value)
print('_'*30)

for key in sorted(dic1.keys(), reverse=True):
    print(key, dic1[key])
print('_'*30)

dic1 = {'a':1, 'b':3, 'c':2, 'd':5}
# 값을 기준으로 오름차순 정렬
for value in sorted(dic1.values()):
    print(value)

# 길이
print(len(dic1))

# 데이터 추가
dic2 = {'e':'파이썬', 'f':'딥러닝'}
dic1['g'] = dic2
print(dic1)

dic1.update(dic2)
print(dic1)





