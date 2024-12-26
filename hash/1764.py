import pandas as pd

# 엑셀 파일 읽기
df = pd.read_excel('data.xlsx')  # 엑셀 파일명을 적절히 수정하세요

# 데이터 가공
# 결측치 처리
df = df.dropna()  # 결측치가 있는 행 제거

# 데이터 타입 변환이 필요한 경우
# df['column_name'] = df['column_name'].astype('int64')  # 예시: 특정 열을 정수형으로 변환

# 중복 제거
df = df.drop_duplicates()

# 필요한 열만 선택
# df = df[['column1', 'column2', 'column3']]  # 필요한 열 이름을 지정

# 데이터 정렬
# df = df.sort_values(by='column_name')

# 기본 통계 정보 확인
print("데이터 기본 정보:")
print(df.info())
print("\n기술 통계량:")
print(df.describe())

# 처리된 데이터 저장
df.to_excel('processed_data.xlsx', index=False)
print("\n가공된 데이터가 'processed_data.xlsx'로 저장되었습니다.")
