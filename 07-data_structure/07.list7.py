kim = [100, 98, 68]
park =[89, 67, 99]
lee = []
for x in range (3): # 3번반복
    lee.append(int(input('점수 :')))    # 점수를 입력받아 lee리스트 맨 뒤에 삽입
print(lee)

hap = [0, 0, 0]
hap[0] = sum(kim)
hap[1] = sum(park)
hap[2] =  sum(lee)

print('김수현의 총점 =', hap[0],  '평균 = %.2f' %(hap[0]/len(kim)))
print(f'박미자의 총점 = {hap[1]} 평균 = {hap[1]/len(park):.2f}')
print(f'이미자의 총점 = {hap[2]} 평균 = {hap[2]/len(lee):.2f}')
