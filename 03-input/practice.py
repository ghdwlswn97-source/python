'''
문
사용자로 부터 입력 받기
    경기장은 어디입니까?
    이긴팀은 어디입니까?
    진팀은 어디입니까?
    스코어는 몇대몇 입니까?

결과는
=========================================
오늘 문학경기장에서 야구경기가 열렸습니다
라이언과 한화의 치열한 공방전이 펼쳐졌습니다
결국 라이언은 한화를 1:3으로 이겼습니다
=========================================
'''

stadium = input('경기장은 어디입니까?')
winner = input('이긴팀은 어디입니까?')
loser = input('진팀은 어디입니까?')
score = input('스코어는 몇대몇 입니까?')


print('=' * 40)
print(f'오늘 {stadium}에서 야구경기가 열렸습니다')
print(f'{winner}과 {loser}의 치열한 공방전이 펼쳐졌습니다')
print(f'결국 {winner}은 {loser}를 {score}으로 이겼습니다')
print('=' * 40)
#  print('오늘', stadium, '에서 야구경기가 열렸습니다')

result = f'''오늘 {stadium}에서 야구경기가 열렸습니다
{winner}과 {loser}의 치열한 공방전이 펼쳐졌습니다
결국 {winner}은 {loser}를 {score}으로 이겼습니다'''
print('=' * 50)
print(result)
print('=' * 50)



# 내 답안
place = input('경기장은 어디입니까?')
win = input('이긴팀은 어디입니까?')
lose = input('진팀은 어디입니까?')
score = input('스코어는 몇대몇 입니까?')

print('오늘' + str(place)+'에서 야구경기가 열렸습니다.\n'
+ str(win)+'과 ' + str(lose)+ '의 치열한 공방전이 펼쳐졌습니다.\n결국'+ str(win)+'은' +str(lose)+'를' + str(score)+'으로 이겼습니다.')


