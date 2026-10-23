'''
문 :
1. 각 클래스의 모든 인스턴스 변수는 private로 변경
2. 추상클래스를 제외한 모든 클래스에서 추상클래스의 인스턴스변수를 호출하여 출력하는 메서드 정의
3. main에서 출력
'''
from programmer import Programmer
from famer import Famer
from actor import Actor
from person import Person


# people = Programmer('김수철', 31, 'python')
# people.introduce()
# print('-'*30)

# people = Actor('박인술', 29, '왕과 사는 남자')
# people.introduce()
# print('-'*30)

# people = Famer('박광덕', 24, '오이')
# people.introduce()
# print('-'*30)

people = [
    Programmer('김수철', 31,'python'),
    Actor('박인술', 29, '왕과사는남자'),
    Famer('박광덕',24,'오이')]

print('======자기소개하기(다형성 활용)======')

for person in people:
    person.introduce()
    print('-'*30)

# actor=Actor
# actor.show_info()

# famer=Famer
# famer.show_info()

# person=Person
# person.show_info()

# programmer = Programmer
# programmer.show_info()