import numpy as np

arr1 = np.array([10, 20, 30, 40, 50, 60])
arr2 = np.arange(10, 100, 10).reshape(3,3)
print(f'arr1 : {arr1}')
print(f'arr2 :\n {arr2}')
print('-'*30)

# 1차원 배열의 인덱싱
print(arr1[0])
print(arr1[[1,3,5]])
print(arr1[arr1 > 30])
print('-'*30)

arr1[2] = 555       # 값 변경
print(f'arr1 : {arr1}')

arr1[[1,3,5]] = [333, 777,999]      # 값 여러개 변경
print(f'arr1 : {arr1}')

arr1[arr1 > 30] = 0
print(f'arr1 : {arr1}')

# 2차원 배열의 인덱싱
print(f'arr2 :\n {arr2}')
print(arr2[0,2])        # 0행의 인덱스 2번
# print(arr2[0][2])
arr2[0,2] = 1000
print(f'arr2 : {arr2}')
print('-'*30)
# 행을 통째로 변경
arr2[1] = [1, 2, 3]
print(f'arr2 : {arr2}')
print('-'*30)

print(arr2[[0,2], [1,1]])       # arr2[[행], [열]] -> 0행의 1열, 2행의 1열
arr2[[0,2],[1,1]] = [100, 200]
print(f'arr2 :\n {arr2}')

