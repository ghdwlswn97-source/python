import numpy as np

arr1 = np.array([[1,2],
                [3,4]])
arr2 = np.array([[5,6],
                [7,8]])

# 행렬곱
print('행렬곱 :')
print(np.dot(arr1, arr2))
print(arr1@arr2)
# [[19 22]    ->  [[(1*5)+(2*7)  (1*6)+(2*8)]
#  [43 50]]        [(3*5)+(4*7)  (3*6)+(4*8)]]
            
# 전치행렬 : 행과 열을 바꿈
print('전치행렬 :')
print(np.transpose(arr1))
print(arr1.T)

# 행렬식 : 행렬이 공간을 얼마나 늘리거나 줄였는지 (확대/축소 비율)
# det() 함수 사용 -> det(A) = 2        
'''
행렬식
행렬이
a b
c d 일 때 
det(A) = a*d-b*c ->  0이면 역행렬은 존재하지 않음
'''
print('행렬식 :')
print(np.linalg.det(arr1))

# 역행렬
'''
A 행렬이 
a   b
c   d 일 때
A의 역행렬은 
d*1/ad-bc   -b*1/ad-bc
-c*1/ad-bc   a*1/ad-bc

1   2
3   4 의 역행렬은
-2     1
1.5   -0.5
'''
print('역행렬')
print(np.linalg.inv(arr1))

if np.linalg.det(arr1) != 0:
    inv_arr1 = np.linalg.inv(arr1)
    print(f'역행렬 : inv_arr1')
    print('검증 :')
    print(arr1@ inv_arr1)
else:
    print('행렬식이 0이므로 역행렬이 존재하지 않습니다.')
