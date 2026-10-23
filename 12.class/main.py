class Triangle:
    def getArea(self, b, h):
        self.b1=b
        self.h1=h
        return self.b1*self.h1/2

# class Tri:
#     @staticmethod
#     def  triangle(x, y):
#         result = x*y/2
#         return result

class Score:
    def set(self):
        self.name = input('이름 :')
        self.python = int(input('파이썬 점수 :'))
        self.ai = int(input('인공지능 점수 :'))
        self.sum = self.python+self.ai
        self.avg = self.sum/2

    def output(self):
        print('이름 :', self.name)
        print('파이썬 : ', self.python)
        print('AI :', self.ai)
        print('합계 :', self.sum)
        print('평균 : ', self.avg)




# class Score:
#     def students(self):
#         self.name= '홍진주'
#         self.python=80
#         self.ai=98

#     def output(self):
#         total = self.python + self.ai
#         agv = total/2

#         print('이름 :', self.name)
#         print('파이썬 : ', self.python)
#         print('AI :', self.ai)
#         print('합계 :', total)
#         print('평균 : ', agv)
        

# myscore=Score()
# myscore.students()
# myscore.output()
        
