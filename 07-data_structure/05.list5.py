list1 = []
list1.append(1)
list1.append(2)
list1.append(3)
list1.append(4)
list1.append(5)
print(list1)

list2 = [1, 2, 3]
list2.append(4)
list2.append(5)
print(list2)

list3 = [1, 2, 3]
list3.append([4, 5])
print(list3) # 중첩리스트 [4, 5]통으로  들어감


list4 = [1, 2, 3]
list4.extend([4, 5])
print(list4)    # 1차원의데이터 맨 뒤에 들어감

list5 = []
for x in range(1, 1001):
    list5.append(x)
print(list5)