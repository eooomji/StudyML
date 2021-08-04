##### 4.15
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data_loc = 'https://github.com/dknife/ML/raw/main/data/'
life = pd.read_csv(data_loc + 'life_expectancy.csv')
# life.head()

### 관심있는 데이터만 추출 + 원하는 열 지정
life = life[['Life expectancy', 'Year', 'Alcohol', 'Percentage expenditure', 'Total expenditure', 'Hepatitis B', 'Measles', 'Polio', 'BMI', 'GDP', 'Thinness 1-19 years', 'Thinness 5-9 years']]
# life.head()

### 데이터 크기, 결손값 살펴보기
# print(life.shape)           # shape : 크기 알 수 있음 => 행, 열로 예상 => 데이터 총 2938개 / 데이터 항목 : 12개
# print('------------------------------')
# print(life.isnull().sum())  # isnull() : 결손값 => isnull에 결손값이 표시되어있음
# print('------------------------------')

### 결손값 있는 데이터 삭제
life.dropna(inplace = True)
# print('결손값 있는 데이터 삭제 후 남은 데이터 크기 :', life.shape)
# print('------------------------------')

# NEW
### 데이터 상관관계 파악 : pairplot
sns.pairplot(life[['Life expectancy', 'Alcohol', 'Percentage expenditure', 'Measles', 'Polio', 'BMI', 'GDP', 'Thinness 1-19 years', 'Thinness 5-9 years']])
plt.show()
