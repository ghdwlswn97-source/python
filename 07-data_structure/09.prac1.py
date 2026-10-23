'''
2차원 리스트로
과정    파이썬 AI 빅데이터 디자인 합계 평균
홍길동  89     100  78      76  ??     ??.?
아무개
이순신
-------------------------------------------
합계    ??                  ??
평균    ??.?               ??.?
'''
# 초기 데이터 설정
students = [
    ['홍길동', 89, 87, 98, 79],
    ['아무개', 86, 84, 45, 84],
    ['이순신', 78, 75, 52, 94],
]

sub_sum = [0, 0, 0, 0]
print('과정\t파이썬\tAI\t빅데이터\t디자인\t합계\t평균')
for row in students:
    name = row[0]
    scores = row[1:]

    for i in range(4):
        sub_sum[i] += scores[i]   


    s_sum = sum(scores)
    s_avg= s_sum / len(scores)

# 학생별 합계
    print(f'{name}\t{scores[0]}\t{scores[1]}\t{scores[2]}\t\t{scores[3]}\t{s_sum}\t{s_avg}')
print('_'*60)

sub_avg = [total /len(students) for total in sub_sum]
print(f'합계\t{sub_sum[0]}\t{sub_sum[1]}\t{sub_sum[2]}\t{sub_sum[3]}')
print(f'합계\t', end='')
for total in sub_sum:
    print(total, end='\t')

print(f'평균\t{sub_avg[0]:.1f}\t{sub_avg[1]:.1f}\t{sub_avg[2]:.1f}\t{sub_avg[3]:.1f}')
print(f'평균\t', end = '')
for avg in sub_avg:
    print(f'{avg:.1f}', end='\t')


name = ['홍길동', '아무개', '이순신']
subjects = ['파이썬', 'AI', '빅데이터', '디자인']
scores = [
    [89, 78, 70, 97],
    [89, 89, 78, 97],
    [98, 98, 90, 89],
    [89, 79, 90, 88]
]
print()
for i in range(3):
    total = sum(scores[i])
    avg = total / len(subjects)

    print(f'{name[i]}\t{scores[i][0]}\t{scores[i][1]}\t{scores[i][2]}\t{scores[i][3]}\t{total}\t{avg:.1f}')

# 과목별
for j in range(4):
    total = 0
    for i in range(3):
        total += scores[i][j]
    print(total, end='\t')

for j in range(4):
    avg = 0
    for i in range(3):
        avg += total/len(subjects)
    print(f'{total/len(subjects)}')