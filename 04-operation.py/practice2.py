# 잔액
balance = 100000

# 구입액
purchase = (900*2) + (3500*5)

# 매출액
sales = (1800*2) + (4000*4) + 1500 + (2000*4) + (1800*5)

# 잔액
balance = balance - purchase + sales

print('오늘 구입액 : ', purchase, '원')
print('오늘 매출액 : ', sales, '원')
print('현재 잔액 : ', balance, '원')



balance = 100000

balance -= 900*10
balance += 1800*2
balance -= 3500*5
balance =+ 4000*4
balance += 1500
balance += 2000*4
balance +=1800*5