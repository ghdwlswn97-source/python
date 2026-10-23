# 가변 키워드 인자
# ** kwargs : dictionary가 전달됨
# 키=값으로 입력
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(key, ':', value)

print_info(name='최명길')
print_info(name='김미영', age='23', city='Seoul')

# 딕셔너리를 넘겨줘도 됨        키:값으로 입력
info = {'name' : '이철수', 'age' : 25, 'city' : 'Gyeongido'}
# ** : 언패킹
print_info(**info)      # == print_info(name='이철수', age=25, city='Gyeongido')
# print_info(info) : error -> info라는 딕셔너리 객체 단 1개를 전달(키=값 형태로 전달해야됨)