import numpy as np
from numpy import random
# 1. 다음 배열에서 정수형 배열을 생성하고, 변환된 배열의 자료형 및 원본 배열 출력
a = np.array([1.8, 2.5, 3.9, 4.2, 5.7])
a1 = a.astype(int)
print(a1.dtype)
print(a1)

# 2.배열만들기
# 2.1. 0 이상 1 미만 실수 난수: 2행 3열
# 2.2. 1 이상 10 이하 정수 난수: 3행 4열
# 2.3. 표준정규분포 난수: 2행 2열
arr1=np.linspace(0,1,6).reshape(2,3)
print(arr1)

arr2=np.linspace(1,11, 12).astype(int).reshape(3,4)
print(arr2)

arr3=random.randn(2,2)
print(arr3)

# 3. 배열 a = [10, 20, 30, 40], b = [2, 4, 5, 8]을 만들고 
#     두 배열의 덧셈, 뺄셈, 곱셈, 나눗셈을 각각 출력
a = [10, 20, 30, 40]
b = [2, 4, 5, 8]
arr4=np.array(a)
arr5=np.array(b)
print(arr4+arr5)
print(arr4-arr5)
print(arr4*arr5)
print(arr4/arr5)


# 4. 배열 [12, 15, 18, 20, 25, 30]의 합계, 평균, 최댓값, 최솟값, 중앙값, 표준편차를 각각 구하기
arr5= np.arange(12,31,5)
print(arr5.sum())
print(arr5.mean())
print(arr5.max())
print(arr5.min())
print(np.median(arr5))
print(arr5.std())


# 5. 다음 2차원 배열의 전체 평균, 행별 평균, 열별 평균, 전체 합계, 행별 합계, 열별 합계를 구하기
a = np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90]])

print(np.mean(a))
print(np.mean(a, axis=1))
print(np.mean(a, axis=0))
print(np.sum(a))
print(np.sum(a, axis=1))
print(np.sum(a, axis=0))


# 6. 다음 배열의 전체 최솟값, 행별 최솟값, 열별 최솟값, 전체 중앙값, 행별 중앙값, 열별 중앙값을 구하기
a = np.array([[8, 3, 5], [2, 9, 4], [7, 1, 6]])
print(np.min(a))
print(np.min(a, axis=1))
print(np.min(a, axis=0))
print(np.median(a))
print(np.median(a, axis=1))
print(np.median(a, axis=0))


# 7. 아래 배열에서 인덱싱과 슬라이싱으로 출력하기
a = np.array([[10, 20, 30, 40],
            [50, 60, 70, 80],
            [90, 100, 110, 120],
            [130, 140, 150, 160]])

# 7.1. 값 70
print(a[1,2])
# 7.2. 첫 번째 행 전체
print(a[:1])
# 7.3. 세 번째 열 전체
print(a[:, 2:3])
# 7.4. 오른쪽 아래 2행 2열
print(a[2,2])
# 7.5. 두 번째~네 번째 행, 두 번째~세 번째 열
print(a[1:, 1:3])


# 8. 행렬 A = [[1, 2], [3, 4]], B = [[5, 6], [7, 8]]에 대해 계산
A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]
a= np.array(A)
b=np.array(B)
# 8.1. A와 B의 행렬곱
print(a@b)
# 8.2. A의 전치행렬
print(np.transpose(a))
# 8.3. B의 전치행렬
print(np.transpose(b))
# 8.4. A * B와 A @ B를 비교
print(a*b)
print(a@b) 
# 9. 행렬 A = [[4, 7], [2, 6]]의 역행렬을 구하고, A와 그 역행렬을 곱해 결과 출력
A = [[4, 7], [2, 6]]
a=np.array(A)
a1 = np.linalg.inv(a)
print(a1)
print(a@a1)

# 10. 아래 배열에서 각 행은 학생, 각 열은 국어·영어·수학 성적
scores = np.array([[80, 90, 70], [60, 75, 85], [95, 80, 90], [70, 85, 75]])

# 10.1. 전체 평균
print(np.mean(scores))
# 10.2. 학생별 평균
print(np.mean(scores, axis=1))
# 10.3. 과목별 평균
print(np.mean(scores, axis=0))
# 10.4. 학생별 최솟값
print(np.min(scores, axis=1))
# 10.5. 과목별 최댓값
print(np.max(scores, axis=0))
# 10.6. 전체 중앙값
print(np.median(scores))
# 10.7. 학생별 중앙값
print(np.median(scores, axis=1))
# 10.8. 과목별 중앙값
print(np.median(scores, axis=0))
# 10.9. 세 번째 학생의 수학 점수
print(scores[2,2])
# 10.10. 첫 번째~두 번째 학생의 영어·수학 점수
print(scores[:2, 1:])
