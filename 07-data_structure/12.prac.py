'''
편의점에서 주말(토요일, 일요일) 알바의 근무시간을 저장한 튜플
            토요일 오전, 토요일 오후, 일요일 오전, 일요일 오후 근무시간
work_hours = (4, 5, 3, 4)
문 1. 주말동안 일한 총 근무시간의합 구하기
문 2. 일요일 근무 시간만 따로 떼어내어 sun_hours라는 새로운 튜츨을 만들어 출력
문 3. 토요일 오전 근무 시간이 4시간에서 5시간으로 변경
'''
work_hours = (4, 5, 3, 4)
# 문1
total = sum(work_hours)
print('총 근무 시간 : ', total)
# 문2
sun_hours = work_hours[2:]
print('일요일 근무시간 :', sun_hours)
# 문3
# 튜플은 수정 불가. 새로운 튜플 만들기
updated_hours = (5,) + work_hours[1:]
print(updated_hours)

