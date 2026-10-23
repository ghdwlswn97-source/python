'''
* set : 중복불가
        순서가 없음(index 없음)
        중괄호{} 사용
        
    *** 주의: 빈 set을 만들 때 {} -> 딕셔너리
            set() -> 빈 set
'''
a = {1, 2, 3, 1, 2, 3, 4, 2, 3}
print(a)        #1, 2, 3, 4 -> 중복불가
print(len(a))

b = {'홍길동', 3, 4, True, (3, 4)}
print(b)        # 순서 상관없이 나옴

c = {}
print(type(c), c)       # 딕셔너리

d= set()
print(type(d), d)       # set
