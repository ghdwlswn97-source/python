'''
문 : 1~100까지 사용자가 넣은 숫자의 배수의 합계를 구하고, 개수는 몇개인지 출력
    조건 : 사용자가 넣은 숫자의 배수만 합계 구하기
    ex) t사용자가 넣은 값 : 7
    7, 14, 21, 28...의 합계
'''

num= int(input('숫자를 입력하세요 :'))
sum = 0
count = 0

for X in range(1,101):
    if X % num==0:
        sum += X
        count += 1

print('1~100까지 사용자가 넣은 숫자의 배수의 합 :', sum) # print(f'1~100까지 {num}의 배수의 합계는 {sum}, 개수는 {count})
print('사용자가 넣은 숫자의 배수의 개수', count)

#2
start = int(input('합계를 구할 시작값 입력 : '))
end = int(input('합계를 구할 끝나는 값 잆력 : '))
num= int(input('숫자를 입력하세요 :'))
sum = 0
count = 0

for X in range(start,end+1):
    if X % num==0:
        sum += X
        count += 1

print('1~100까지 사용자가 넣은 숫자의 배수의 합 :', sum) # print(f'1~100까지 {num}의 배수의 합계는 {sum}, 개수는 {count})
print('사용자가 넣은 숫자의 배수의 개수', count)