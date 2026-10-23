'''
pandas API : 데이터 분석 및 조작을 위한 라이브러리
    > CSV, Excel, json, SQL등 다양한 형식의 데이터를 쉽게 읽어올 수 있다
    > 결측치(빈데이터) 채우기/삭제, 중복 데이터 제거, 타입 변환 등의 전처리가 용이
    > 대용량 데이터도 빠르게 처리
'''
import pandas as pd

fileName = '11.file/data/students.xlsx'

# 엑셀 파일 읽어오기(첫번째 시트를 기본으로 읽음)
df = pd.read_excel(fileName) # df = pd.read_excel('11.file/data/students.xlsx',sheet_name='시트이름') -> 원하는 시트불러오기
print(df)
print(df.head()) #상위 5개 행만 출력(표형태 확인용)
print('='*50)

fileName = '11.file/data/data.json'
df= pd.read_json(fileName)
print(df)
print('='*50)

fileName = '11.file/data/data_list.json'
df= pd.read_json(fileName)
print(df)
print('='*50)

fileName = '11.file/data/data_list2.json'
df= pd.read_json(fileName)
print(df)
print('='*50)

# 일반 json 모듈로 파일을 읽어서 딕셔너리로 가져오기
import json
fileName = '11.file/data/data.json'
with open(fileName, 'r',encoding='utf=8') as f:
    data = json.load(f)

df = pd.DataFrame([data])
print(df)