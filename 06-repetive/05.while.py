sum =0
for i in range(1, 101):
    sum+= i
print(sum)

'''
초기값
while 조건식(참) :
    실행문
    증가값
'''

i = 1
sum = 0
while i <= 100 :
    sum += i
    i += 1
print(sum)


total = 0
i = 1
while True:     # 무한반복
    if i > 100 : 
        break
    total += i
    i += 1
print(f'1~100까지 합 : {total}')
