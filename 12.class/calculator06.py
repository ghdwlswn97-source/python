class Calculator:
    def plus(self, x, y):
        return x+y
    
    def minus(self, x, y):
        return x-y
    
    def multi(self, x, y):
        return x*y

    def divide(self, x, y):
        return x/y

if __name__=='__main__':
    cal = Calculator()
    print(cal.plus(3,5))
    