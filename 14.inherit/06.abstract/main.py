'''
* 추상클래스
    : 추상 메서드가 포함되어 있는 클래서
        > 추상 메서드 : 구현하지 않은 메서드
    - 추상클래스를 상속받는 클래스는 반드시 추상 메서드를 구현해야 한다.
    - 추상클래스는 객체를 생성할 수 없다.

* 추상클래스를 만드는 방법    
    - abc : Abstract Base Class(추상 기본 클래스)의 약자
            파이썬에서 추상 클래스를 정의 할 때 사용하는 내장 모듈
    - ABC : abc모듈에 들어있는 클래스
    - abstractmethod : 추상메서드 위에 @abstractmethod 어노테이션을 달아야 한다

    - 추상클래스는 import를 반드시 해야한다.
        from abc import ABC, abstractmethod 
    -  본 클래스에서는 ABC 클래스를 상속 받아야한다.
        class 클래스명(ABC)
'''

from programmer import Programmer
from famer import Famer
from actor import Actor

kim = Programmer('김수철', 31, 'python')
kim.introduce()

park = Actor('박수철', 28, '오딧세이')
park.introduce()

# lee = Famer('이수철', 29, '당근')
# lee.introduce()
# lee.show()

# # 추상클래스는 객체 생성 못함
# from person import Person
# person = Person()     error
