'''
은행 : 개설할 때 계좌주 이름과 초기 예금액을 넣어줌
        입금하면 잔고 변경
        출금 잔고 변경(찾는금액 잔액보다 많으면 출금안되게 출력'잔액부족')
        
        [???님의 계좌 정보] (현재 잔액 : ???원)
'''
class BankAcount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
        print(f'{self.owner}님의 계좌가 개설되었습니다. 현재잔액은 {self.balance}원')

    def deposit(self, amount):
        self.balance += amount
        print(f'{amount}원이 입금 되었습니다.')

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print('잔액이 부족합니다.')

    def __str__(self):
        return f'[{self.owner}님의 계좌 정보] 현재 잔액 : {self.balance}원'

b1 = BankAcount('홍길동', 10000)
b2 = BankAcount('김철수')
b1.withdraw(20000)
b2.deposit(20000)

b1.deposit(20000)
b1.withdraw(15000)
b2.withdraw(10000)
print(b1)
print(b2)




# def bank():
#     name =input('이름을 입력하세요 :')
#     balance = int(input('초기 예금액을 입력하세요 :'))
#     print(f'계좌주 : {name}, 초기 예금액 : {balance}')
#     return balance

# def insert(balance):
#     insert_coin=int(input('입금 금액을 입력하세요 :'))
#     balance += insert_coin
#     print(f'입금 후 잔액 : {balance}')
#     return balance

# def output(balance):
        
#     output_coin=int(input('출금 금액을 입력하세요 :'))

#     if output_coin>balance:
#         print('잔액이 부족합니다.')
#         return balance
    
#     balance -= output_coin
#     print(f'출금 후 잔액 : {balance}')
#     return balance

# def __str__(self):
#     result=f'[{bank.name}님의 계좌정보] 현재 잔액 : {balance}원'
#     return result

    

# balance=0
# insert_coin=0
# output_coin=0
# balance=bank()
# balance=insert(balance)
# balance=output(balance)

