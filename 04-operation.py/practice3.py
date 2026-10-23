python = 3
os = 2
ai = 3

A = 4.5
A0 = 4
B = 3.5
B0 = 3

total_points = (python* A) + (os *B0) + (ai * A0)
total_credits =  python + os + ai
avg_credits = total_points / total_credits
print(f'총 이수 학점 : {total_credits}학점')
print(f'평균 학점 : {avg_credits:.2f}')