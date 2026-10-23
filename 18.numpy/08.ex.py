'''
연습문제
1. 1차원 배열 만들기
NumPy를 사용하여 1차원 배열 생성
[10 20 30 40 50]

2. 2차원 배열 만들기
NumPy를 사용하여  2차원 배열 생성
[[1 2 3]
 [4 5 6]]

3. arange()를 사용하여 5부터 20까지 3씩 증가하는 1차원 배열을 생성

4. arange()로 1부터 12까지의 숫자를 생성한 뒤, reshape()를 이용하여 3행 4열의 배열로 변환

5. linspace()를 이용하여 0부터 1까지 동일한 간격으로 나누어진 숫자 6개를 생성

6. 모든 원소가 0인 3행 4열의 배열 생성

7. 모든 원소가 1인 2행 5열의 배열 생성. 단, 데이터 타입은 정수형으로

8. 다음 조건을 만족하는 배열 생성
- 2부터 24까지 짝수를 생성
- 생성한 배열을 3행 4열로 변환한다.

9. 다음 조건을 만족하는 배열을 생성
- 10부터 50까지 균등한 간격의 숫자 9개를 생성
- 생성한 배열을 3행 3열로 변환

10. 다음 세 가지 배열을 각각 생성
1. arange()와 reshape()를 사용해 1부터 16까지의 숫자를 4행 4열로 만든다.
2. 모든 원소가 0인 4행 4열의 배열을 만든다.
3. 모든 원소가 1인 4행 4열의 정수형 배열을 만든다.

11. 4행 4열의 단위행렬을 생성(자료형 정수형(int))

12. 3행 5열의 배열에서 주대각선보다 한 칸 오른쪽에 1이 위치하도록 만들기
    자료형은 정수형으로 지정
'''
import numpy as np

arr1=np.array([10,20,30,40,50])
# arr1=np.arange(10, 51, 10)
print(arr1)



arr2=np.arange(1,7)
arr3=arr2.reshape(2,3)      # -> arr2 = np.arange(1,7).arr2.reshape(2,3)
print(arr3)

arr4=np.arange(5,21,3)
print(arr4)

arr5=np.arange(1,13)
arr6=arr5.reshape(3,4)
print(arr6)

print(np.linspace(0,1, 6))

arr7=np.zeros((3,4))
print(arr7)

arr8=np.ones((2,5), dtype=int)
print(arr8)

arr9=np.arange(2,25,2)
print(arr9)
arr10=arr9.reshape(3,4)
print(arr10)

arr11=np.linspace(10,51,9)
arr12=arr11.reshape(3,3)
print(arr12)

arr13=np.arange(1,17)
arr14=arr13.reshape(4,4)
print(arr14)

arr15=np.zeros((4,4))
print(arr15)

arr16=np.ones((4,4), dtype=int)
print(arr16)

print(np.identity(4, dtype=int))

arr17=np.eye(3,5, 1, dtype=int)
print(arr17)