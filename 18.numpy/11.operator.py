import numpy as np

data1 = [10,20,30,40]
data2 = [100, 200, 300, 400]

# 리스트에서 결합
list1 = data1+data2
print(list1)        # [10, 20, 30, 40, 100, 200, 300, 400]

# numpy 연산
arr1 = np.array(data1)
arr2 = np.array(data2)

r1 = arr1 + arr2
print(r1)       # [110 220 330 440]

r2 = arr1 - arr2
print(r2)

r3 = arr1 * arr2
print(r3)

r4 = arr1 / arr2
print(r4)

r5 = arr1 + 5
print(r5)       # [15 25 35 45]

r6 = arr1**2
print(r6)       #[ 100  400  900 1600]

