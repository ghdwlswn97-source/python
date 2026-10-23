'''
students = []
with open('11.file/test.csv', 'r') as f:
    lines = f.read().splitlines()
    # lines = f.readlines()
    print(lines)

    for line in lines:
        # line = line.strip()       # \n 없애기
        # print(line)
        # line = line.split(',')    # , 기준으로 나누기
        # print(line)
        # students.append(line)     # students = [] 리스트에 넣기

        # 3줄을 한줄로
        students.append(line.strip().split(','))

print(students)

students2 = []
with open('11.file/test.csv', 'r') as f:
    lines = f.read().splitlines()
    # lines = f.readlines()
    print(lines)

    for line in lines:
        # line = line.split(',')       
        # print(line)
        # students2.append(line)

        # 위의 2줄을 한줄로
        students2.append(line.split(','))

print(students2)
'''


students3 = []
with open('11.file/test.csv', 'r') as f:
    lines = f.read().splitlines()
    print(lines)

    for line in lines:
        # line = line.split(',')       
        # print(line)
        # students3.append(line)

        # 위의 2줄을 한줄로
        students3.append(line.split(','))
print(students3)
# 위를 comprehension으로 나타내기
with open('11.file/test.csv', 'r') as f:
    students3 = [ line.split(',') for line in f.read().splitlines()]  
print(students3)


#문제 이름 : 더조은, 국어 : 90, 영어::80, 수학:80, 총점:87.2, 평균:85
result=0
for student in students3:
    name, kor, eng,  math = student
    total = int(kor)+int(eng)+int(math)
    avg = total/3

    result += f'이름:{name}, 국어:{kor}, 영어:{eng}, 수학:{math}, 총점:{total}, 평균:{avg:.1f}\n'

print(result)

with open('11.file/result.txt', 'w') as f:
    f.write(result)


