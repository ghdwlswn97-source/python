class SeatAlreadyError(Exception):
    def __init__(self, seat_num):
        super().__init__(f'{seat_num}번 좌석은 이미 예약되었습니다.')

class SeatNotError(Exception):
    def __init__(self, seat_num):
        super().__init__(f'{seat_num}번 좌석은 유효하지 않습니다.')