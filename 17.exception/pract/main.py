from exceptions import SeatAlreadyError, SeatNotError
from movie import Movie

movie = Movie('아바타4',10)

try:
    movie.reserve(3)
    movie.reserve(7)
    movie.reserve(1)
except (SeatAlreadyError, SeatNotError, ValueError) as e:
    print('[처리 실패]', e)

movie.show()

try:
    movie.cancel(3)
    movie.cancel(5)
except (SeatAlreadyError, SeatNotError, ValueError) as e:
    print('[처리 실패]', e)
