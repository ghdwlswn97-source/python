import my_module3

print(f'{my_module3.add(3,5)}')
print(my_module3.sub(4,2))
print(my_module3.random_num)
my_module3.count = 5
# 클래스 호출 시 객체 생성
student = my_module3.Student('김마리', 25)
student.introduce()
#추상메서드는 객체 X
my_module3.Student.hello()
# 람다함수호출
print(my_module3.square(5))
