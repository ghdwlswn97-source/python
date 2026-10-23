st1= 'He likes apples, and she does, too'

# split() : 특정문자 기준으로 문자열 분리
# 기본값 : 공백문자
# 결과값 : 리스트

st2=st1.split()
print(st1)
print(st2)
print('_'*40)

# 콤마, 를 기준으로 분리
st2 = st1.split(',')
print(st2)
print('_'*40)

# 공백을 기준으로 3번만 분리
st2 =st1.split(' ',3)
print(st2)
print('_'*40)

st2 = st1.split()
st3=', '.join(st2)
print(st2)
print(st3)
print('_'*40)
