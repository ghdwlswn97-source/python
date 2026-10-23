'''
custom except
1. 좌석이 예약된 상태에서 좌석 선택했을 때
2. 없는 좌석번호로 예약할 때

class 
1. 초기화 영화제목, 총좌석
2. 좌석이 유효한 좌석인지
    좌석이 있으면 예약되는것, 없는좌석은 예외발생
3. 예약
    예약하기. 이미 예약된 좌석이라면 1번 except 발생
4. 예약취소
5. 출력하기
    영화 : ???
    예약된 좌석: ???
'''

from custom_except import SeatError, InvalidSeatError, Movie

movie = Movie('어벤져스', 3)

try:
    movie.reserve(1)
    movie.reserve(3)
    movie.reserve(1)
except SeatError as s:
    print(s)
except InvalidSeatError as  i:
    print(i)


try:
    movie.reserve(7)
except SeatError as s:
    print(s)
except InvalidSeatError as i:
    print(i)

movie.cancle(3)

movie.show()
