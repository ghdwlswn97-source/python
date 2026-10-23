str_list = ['국어', '영어', '수학', '국사', '컴퓨터']
print(str_list.index('영어'))
# print(str_list.index('파이썬'))       # 데이터 없으면 오류

a = '파이썬'
if a in str_list:
    print(str_list.index(a))
else :
    print('데이터 없음')

# 항목 추가 : 제일 뒤에 데이터 추가(append)
str_list.append('파이썬')
print(str_list)

# 데이터를 중간에 삽입(insert)
str_list.insert(2, '인공지능')
print(str_list)
print('_' *30)

# 데이터 정렬
# sorted : 데이터 원본은 안바뀜
print(sorted(str_list)) # ㄱ, ㄴ, ㄷ/a, b, c 오름차순 정렬
print(sorted(str_list, reverse = True)) # 내림차순
print(str_list)
print('_' *30)
# sort : 데이터 원본이 바뀜
str_list.sort() # 오름차순
print(str_list)

str_list.sort(reverse= True)    # 내림차순
print(str_list)

# 데이터 삭제 없는 데이터 넣으면 에러
# if '삭제요소' in 리스트
if '국어' in str_list:
    str_list.remove('국어')
print(str_list)

# 모든 데이터 삭제
str_list.clear()
print(str_list)