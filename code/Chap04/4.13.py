##### 4.13 setting
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data_loc = 'https://github.com/dknife/ML/raw/main/data/'
life = pd.read_csv(data_loc + 'life_expectancy.csv')
# life.head()

### 관심있는 데이터만 추출 + 원하는 열 지정
life = life[['Life expectancy', 'Year', 'Alcohol', 'Percentage expenditure', 'Total expenditure', 'Hepatitis B', 'Measles', 'Polio', 'BMI', 'GDP', 'Thinness 1-19 years', 'Thinness 5-9 years']]
# life.head()
