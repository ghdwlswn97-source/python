from exceptions import SeatAlreadyError, SeatNotError

class Movie:
    def __init__(self, movie_title, total_seats):
        self.movie_title = movie_title
        self.total_seats = total_seats
        self.reserved_seats= []

    def validate_seat(self, seat_num):
        if not 1<= seat_num <= self.total_seats:
            raise ValueError('존재하지 않는 좌석 번호 입니다.')

    def reserve(self, seat_num):
        self.validate_seat(seat_num)
        if seat_num in self.reserved_seats:
            raise SeatAlreadyError(seat_num)

        self.reserved_seats.append(seat_num)
        print(f'{seat_num}번 예약 완료')
    
    def cancel(self, seat_num):
        self.validate_seat(seat_num)
        if seat_num not in self.reserved_seats:
            raise SeatNotError(seat_num)

        self.reserved_seats.remove(seat_num)
        print(f'{seat_num}번 예약 취소 완료')

    def show(self):
        print(f'영화 : {self.movie_title}')
        print(f'예약된 좌석 : {sorted(self.reserved_seats)}')


