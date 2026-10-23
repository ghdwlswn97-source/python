st1= '              He likes apples, and she does,  too     '

# 좌우 공백 제거
st2=st1.strip()
print(st1,'===')
print(st2,'====')
print('_'*30)

# 오른쪽  공백 제거
st2=st1.rstrip()
print(st1,'===')
print(st2,'====')
print('_'*30)

# 왼쪽 공백 제거
st2=st1.lstrip()
print(st1,'===')
print(st2,'====')
print('_'*30)

# 문자열 바꾸기
st2=st1.replace('like', 'love')
print(st2)
print('_'*30)

st2=st1.replace('like', 'love', 1)  # 횟수 지정
print(st1)
print(st2)
print('_'*30)

st2=st1.replace(' ','') # 공백 제거
print(st1)
print(st2)