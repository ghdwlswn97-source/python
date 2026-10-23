import student

name = '김수완'
# *args 일 때
# avg = student.average( 90, 87, 48, 47)
# **kwargs일 때
avg = student.average(kor = 90, eng=87, math=48, com=47)

grade = student.get_grade(avg)

# print('이름 : ', '김수완')
# print('평균점수 :', avg)
# print('학점 : ', grade)
student.print_info(name, avg, grade)
