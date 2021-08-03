import matplotlib.pyplot as plt
import pandas as pd

data_home = 'https://github.com/dknife/ML/raw/main/data/'
lin_data = pd.read_csv(data_home+'pollution.csv')

def h(x, param):
  return param[0]*x + param[1]

learning_iteration = 1000   # 학습 반복 횟수
learning_rate = 0.0025      # 학습율

param = [1, 1]              # w, b를 하나의 변수

x = lin_data['input'].to_numpy()  # to_numpy : pandas 객체를 numpy 배열 객체인 ndarray로 반환
y = lin_data['pollution'].to_numpy()

for i in range(learning_iteration):
  if i % 200 == 0:
    lin_data.plot(kind = 'scatter', x = 'input', y = 'pollution')
    plt.plot([0, 1], [h(0, param), h(1, param)])
  error = (h(x, param) - y)
  param[0] -= learning_rate * (error * x).sum()
  param[1] -= learning_rate * error.sum()
