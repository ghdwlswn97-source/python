import json

# encoding 함수
def enco(file_path):
    encodings = ['UTF=8', 'EUC-KR', 'CP949']

    for enc in encodings:
        try:
            with open(file_path, 'r', encoding=enc) as f:
                return enc
        except UnicodeDecodeError:
            continue

# data.jsom 한개의 {}만 있을 때 파일 가져오기
files = '11.file/data/data.json'
with open(files, 'r', encoding='utf-8') as f:
    data = json.load(f)

print(data)
print(type(data))

print(f'이름 : {data['name']}')
print(f'보유기술 : {data['skills']}')       # 보유기술 : ['Python', 'HTML', 'SQL']
print(f'보유기술 : {data['skills'][0]}')    # 보유기술 : Python 뒤에 인덱스 추가하면 원하는 값만 가져올수있음

# data2.jsom 여러개의 {}가 있을 때 파일 가져오기
students = []
add_string = ''
files = '11.file/data/data2.json'
with open(files, 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip()
        add_string += line

        if line == '}':
            student_dic = json.loads(add_string)
            students.append(student_dic)

            add_string=''

print('===== [변환된 students 리스트] =====')
print(students)
print('===== [한명씩 출력] =====')
for std in students:
    # print(f'이름 : {std['name']} | 나이 : {std['age']}세 | 보유기술 : {std['skills']}')
    print(f'이름 : {std['name']} | 나이 : {std['age']}세 | 보유기술 : {','.join(std['skills'])}')
print('-'*50)
# if not line:
students=[]
add_string=''
files = '11.file/data/data3.json'
with open(files, 'r', encoding= 'utf-8') as f:
    for line in f:
        if not line:        # 바닥(빈행을 만날 때)
            continue

        line = line.strip()
        add_string += line

        if line =='}':
            student_dic=json.loads(add_string)
            students.append(student_dic)

            add_string=''

print('===== [변환된 students 리스트]')
print(students)
print('===== [한명씩 출력] =====')
for std in students:
    print(f'이름 : {std['name']} | 나이 : {std['age']}세 | 보유기술 : {std['skills']}')
