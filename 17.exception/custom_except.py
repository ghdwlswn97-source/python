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
class SeatError(Exception):
    def __init__(self, seat):
        super().__init__(f'{seat}번 좌석은 이미 예약되었습니다')

class InvalidSeatError(Exception):
    def __init__(self, seat):
        super().__init__(f'{seat}번 좌석은 없는 좌석번호입니다.')


class Movie:
    def __init__(self, title, total_seat):
        self.title =  title
        self.total_seat = total_seat
        self.reserved_seat = []

    def check_seat(self, seat):
        if seat <1 or seat> self.total_seat:
            raise InvalidSeatError

    def reserve(self, seat):
        self.check_seat(seat)

        if seat in self.reserved_seats:
            raise SeatError(seat)
        
        self.reserved_seat.append(seat)
        print(f'{seat}번 좌석 예약완료')

    def cancle(self, seat):
        self.check_seat(seat)

        if seat in self.reserved_seat:
            self.reserved_seat.remove(seat)
            print(f'{seat}번 좌석 예약이 취소 됐습니다.')

        else:
            print(f'{seat}번 좌석은 예약되어있지 않습니다.')

    def show(self):
        print(f'영화 : {self.title}')
        print(f'예약된 좌석 : {self.reserved_seat}')


        

