# tuple : 리스트와 동일하지만 변경 불가
# 소괄호() -> 안써도 됨

tup1 = (10, 20, 30, 40)
tup2 = ('python', 4.56, 98, True)
tup3 = 'python', 4.56, 98, True
print('tup3의 type = ', type(tup3))

# 데이터가 1개 일 때  
tup4 = (10,)
tup5 = 30,
tup6 = 20

print('tup4의 type = ', type(tup4))
print('tup5의 type = ', type(tup5))
print('tup6의 type = ', type(tup6))
print('_'*30)

print(tup1[1])
print(tup3[3])
print('_'*30)

# error
# tup1[1] = 100
# tup1.clear()