def get_grade(score):


    if score >100 or score <0:
        print('잘못된점수입니다')
    elif score>=90:
        return 'A학점'
    elif score>=80:
        return 'B학점'
    elif score>=70:
        return 'C학점'
    elif score>=60:
        return 'D학점'
    else:
        return'F학점'
