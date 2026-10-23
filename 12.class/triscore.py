# 문 1
from  main import Triangle as t
b= int(input('밑변 :'))
h = int(input('높이 :'))

area= t()
print(area.getArea(b, h))

# from  main import Tri
# print(Tri.triangle(3,4))

# 문2
from main import Score as sc
sc1 = sc()
sc2=sc()

sc1.set()
sc2.set()

sc1.output()
print()
sc2.output()
