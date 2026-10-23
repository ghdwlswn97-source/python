st1= 'He likes apples, and she does, too'

# 문자열에서 특정 문자열의 개수를 구하기
print(st1.count('like'))

# 왼쪽에서 오른쪽으로 문자열을 검색
p= st1.find('like')
print(p)    # index 번호 3
print(st1.find('like', p+1))    # 두번째 like의 index 번호
print(st1.find('love'))     # 데이터가 없으면 -1로 표시

# 오른쪽에서 왼쪽으로 문자열 검색
p = st1.rfind('like')
print(p)
print(st1.rfind('like',0,p))

# index() : find()와 기능은 같지만 없으면 예외 발생
p = st1.index('like')
print(p)
# print(st1.index('love'))

# 시작하는 단어인지 검사
print(st1.startswith('likes'))
print(st1.startswith('likes',3))

# 끝나는 단어인지 검사
print(st1.endswith('likes'))
print(st1.endswith('too'))
print(st1.endswith('likes',0,8))
