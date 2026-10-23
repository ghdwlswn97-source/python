# 예외처리 : try - except - finally(생략가능)

try : 
    # 예외가 발생할 가능성이 있는 코드
    result = 10/0
    print(result)
    print('try에서 실행됨')
except:
    # 예외가 발생했을 때 실행 할 코드
    print('오류 발생. 0으로 나눌 수 없음')

print('프로그램 끝')

# try :
#     num= int(input('숫자입력 :'))
#     result = 10/num
# except ValueError:
#     print('숫자만 입력해야 됩니다')
# except ZeroDivisionError:
#     print('0으로 나누 수 없음')

# print(result)

try:
    f = open('17.exception/data.txt', 'r')

except FileNotFoundError :
    print('파일이 존재하지 않습니다.')
else :
    print('파일을 성공적으로 읽었습니다.')
finally:
    print('작업을 끝냅니다.')       # 오류가 나든안나든 출력
