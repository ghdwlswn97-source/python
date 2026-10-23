from datetime import datetime

# 현재시간
print(datetime.now())

d = datetime(2026,10,8,14,4,4)

print(d)

print(f'{d:%Y/%m/%d}')
print(f'{d.hour}:{d.minute}:{d.second}')

# H :24시간제
print(f'{d:%H:%M:%S}')       #14:04:04

# I : 12 시간제, P:AM, PM
print(f'{d:%I:%M:%S %p}')       #02:04:04 PM

# 일수계산
day1 = datetime(2026, 10, 1)
day_num = datetime.now() -day1
print(day_num)

day_num = (datetime.now()-day1).days
print(f'일수 : {day_num}일')