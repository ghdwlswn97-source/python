# 1~100 합계
sum = 0 # 초기화 필수
for i in range(1,101):
    sum+= i
print(sum)

# 1~100까지 5의 배수의 합
#1
sum = 0
for s in range(1, 101):
    if s%5==0 :
        sum +=s

print('1~100까지 5의 배수의 합 :', sum)

#2
sum=0
for n in range(0, 101, 5):
    sum += n

print('0~100까지 5의 배수의 합 :', sum)
