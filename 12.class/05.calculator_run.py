# 다른클래스 사용할 때
# 1) import 파일명
# 2) from 파일명 import 클래스명

# 1)
import calculator05
cal1 = calculator05.Calculator()
print(cal1.plus(10,20))
print(cal1.multi(10,20))

# 2)
from calculator05 import Calculator
cal2 = Calculator()
print(cal2.plus(10,20))
print(cal2.multi(10,20))

# 3)
from calculator05 import Calculator as c        # 이름이 길 때 'as 별칭 ' 
cal3 = c()
print(cal3.plus(10,20))
print(cal3.multi(10,20))
