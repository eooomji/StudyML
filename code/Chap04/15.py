import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data_loc = 'https://github.com/dknife/ML/raw/main/data/'
life = pd.read_csv(data_loc + 'life_expectancy.csv')

### 관심있는 데이터만 추출 + 원하는 열 지정
life = life[['Life expectancy', 'Year', 'Alcohol', 'Percentage expenditure', 'Total expenditure', 'Hepatitis B', 'Measles', 'Polio', 'BMI', 'GDP', 'Thinness 1-19 years', 'Thinness 5-9 years']]

### 결손값 있는 데이터 삭제
life.dropna(inplace = True)

# NEW
### 데이터 상관관계 파악 : pairplot
sns.pairplot(life[['Life expectancy', 'Alcohol', 'Percentage expenditure', 'Measles', 'Polio', 'BMI', 'GDP', 'Thinness 1-19 years', 'Thinness 5-9 years']])
plt.show()
