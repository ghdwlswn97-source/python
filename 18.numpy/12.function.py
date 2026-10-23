import numpy as np

arr1 = np.arange(10, 61, 10)
print(arr1)
# [10 20 30 40 50 60]

print(f'합계 : {arr1.sum()}')
print(f'평균 : {arr1.mean()}')
print(f'분산 : {arr1.var()}')       # 0에 가까울 수록 모여있음
print(f'표준편차 : {arr1.std()}')       # 작을수록 표준에 모여있음
print(f'최소값 : {arr1.min()}')
print(f'최대값 : {arr1.max()}')
print(f'누적합 : {arr1.cumsum()}')      # 누적합 : [ 10  30  60 100 150 210]
print(f'누적곱 : {arr1.cumprod()}')     # 누적곱 : [       10       200      6000    240000  12000000 720000000]
print('-'*30)

print(f'합계 : {np.sum(arr1)}')
print(f'평균 : {np.mean(arr1)}')
print(f'분산 : {np.var(arr1)}')       # 0에 가까울 수록 모여있음
print(f'표준편차 : {np.std(arr1)}')       # 작을수록 표준에 모여있음
print(f'최소값 : {np.min(arr1)}')
print(f'최대값 : {np.max(arr1)}')
print(f'누적합 : {np.cumsum(arr1)}')      # 누적합 : [ 10  30  60 100 150 210]
print(f'누적곱 : {np.cumprod(arr1)}')     # 누적곱 : [       10       200      6000    240000  12000000 720000000]
print('-'*30)

# 2차원 배열의 평균
arr2 = arr1.reshape(2,3)
print(f'arr2 : \n{arr2}')
#[[10 20 30]
#  [40 50 60]]
'''
2차원
axis = 0 열
axis = 1 행
    
3차원
axis = 0 층
axis = 1 행
axis = 2 열
'''
print(f'전체평균 : {np.mean(arr2)}')
print(f'전체평균 : {arr2.mean()}')
print(f'행 평균 : {np.mean(arr2, axis=1)}')     # 행 평균 : [20. 50.]
print(f'열 평균 : {np.mean(arr2, axis=0)}')     # 열 평균 : [25. 35. 45.]


print(f'최소값 : {np.min(arr2)}')
print(f'최소값 : {np.min(arr2, axis=1)}')
print(f'최소값 : {np.min(arr2, axis=0)}')

print(f'최대값 : {np.max(arr2)}')
print(f'최대값 : {np.max(arr2, axis=1)}')
print(f'최대값 : {np.max(arr2, axis=0)}')

# 중앙값 : median() -> 정렬한 후 중앙값 추출
arr3 = np.array([1, 100, 2])        # 중앙값 : 2    -> 홀수이면 가운데값 출력
arr3 = np.array([1, 100, 2, 80])        # 중앙값 : 41   -> 짝수이면 가운데값 2개 평균
print(f'중앙값 : {np.median(arr3)}')

arr4 = np.array([1,100,4,2])
print(f'중앙값 : {np.median(arr4)}')        # 중앙값 : 2와 4의 평균인 3

# 2차원 배열의 축 별 중앙값
arr5 = np.array([[1,2,3],
                [10,20,30]])
# 전체 중앙값
print(f'전체 중앙값 : {np.median(arr5)}')
# 행 별 중앙값
print(f'행 별 중앙값 : {np.median(arr5, axis=1)}')
# 열 별 중앙값
print(f'행 별 중앙값 : {np.median(arr5, axis=0)}')
