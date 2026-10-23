jumsu = 81

if jumsu >= 90:        #90보다 큰값은 모두 다
    print('A학점')
else :                  # 90미만인 모든 값
    if jumsu >= 80:     # 90 미만, 80이상
        print('B학점')
    else:               # 80 미만인 모든 값
        if jumsu >=70:
            print('C학점')
        else:
            if jumsu >= 60:
                print('D학점')
            else:
                print('F학점')

if jumsu >= 90 and jumsu <=100:
    print('A학점')
elif jumsu >=80:
    print('B학점')
elif jumsu >=70:
    print('C학점')
elif jumsu >=60:
    print('D학점')
elif jumsu >=0:
    print('F학점')

