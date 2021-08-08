import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

HorsePower2 = pd.Series([130, 250, 190, 300, 210, 220, 170])
Efficiency2 = pd.Series([16.3, 10.2, 11.1, 7.1, 12.1, 13.2, 14.2])

PCC = pd.DataFrame({'horsePower' : HorsePower, 'efficiency' : Efficiency})

x = PCC['horsePower'].to_numpy()
y = PCC['efficiency'].to_numpy()
x = x[:, np.newaxis]  # (기존+1)차원 배열이 됨

LR = LinearRegression()
result = LR.fit(x,y)
print('계수 :', result.coef_)
print('절편 :', result.intercept_)
print('예측 점수 :', result.score(x,y))
