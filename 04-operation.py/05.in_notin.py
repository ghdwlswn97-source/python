'''
소속연산자
in : 어떤 데이터가 특정 데이터안에 있는지 검사
        -> True : 있다
        -> False : 없다

not in: 어떤 데이터가 특정 데이터안에 없는지 검사
        -> True : 없다
        -> False : 있다
'''
str = 'abcdefghi'
print('bc' in str)
print('bf' in str)
print('mn' in str)
print('_' *30)

print('bc' not in str)
print('bf' not in str)
print('mn' not in str)