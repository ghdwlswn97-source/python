st1= '12345' 
st2 = 'PythonAi'
st3 = 'Python Ai'
st4 = '이정은'
st5 = '1234abcd'


# 숫자만으로 구성되어 있는지검사
print('숫자로만 구성되어 있는가?', st1.isdigit())
print('숫자로만 구성되어 있는가?', st2.isdigit())
print('숫자로만 구성되어 있는가?', st5.isdigit())
print('_'*40)

# 문자로만 구성되어 있는지 검사 공백 : 문자로 인정 안함
print('문자로만 구성되어 있는가?', st1.isalpha())
print('문자로만 구성되어 있는가?', st2.isalpha())
print('문자로만 구성되어 있는가?', st3.isalpha())   
print('문자로만 구성되어 있는가?', st4.isalpha())
print('문자로만 구성되어 있는가?', st5.isalpha())
print('_'*40)

# 숫자나 문자로 구성되어 있는지검사
print('숫자나 문자로 구성되어 이는가?', st1.isalnum())
print('숫자나 문자로 구성되어 이는가?', st2.isalnum())
print('숫자나 문자로 구성되어 이는가?', st3.isalnum())
print('숫자나 문자로 구성되어 이는가?', st4.isalnum())
print('숫자나 문자로 구성되어 이는가?', st5.isalnum())
print('_'*40)

# 문자열이 소문자인지 검사
st6=st2.lower()
st7= st3.lower()
print('문자열이 소문자인가?', st1.islower())
print('문자열이 소문자인가?', st2.islower())
print('문자열이 소문자인가?', st3.islower())
print('문자열이 소문자인가?', st4.islower())
print('문자열이 소문자인가?', st5.islower())
print('문자열이 소문자인가?', st6.islower())
print('문자열이 소문자인가?', st7.islower())
print('_'*40)

# 문자열이 공백문자인지 검사
st6='          '
print('문자열이 공백문자인가?', st6.isspace())
print('_'*40)

# 단어의 첫글자가 대문자인지 검사(첫글자만 대문자인지. 중간에 대문자있으면 False)
print('단어의 첫글자가 대문자인가?', st1.istitle())
print('단어의 첫글자가 대문자인가?', st2.istitle())
print('단어의 첫글자가 대문자인가?', st3.istitle())
print('단어의 첫글자가 대문자인가?', st4.istitle())
print('단어의 첫글자가 대문자인가?', st5.istitle())
print('_'*40)

# 빈자리를 0으로 채우기
st1 ='Hello Python!!!'
st2 = st1.zfill(20)
print(st1)
print(st2)


