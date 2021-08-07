import numpy as np
from sklearn.neighbors import KNeighborsClassifier

# 닥스훈트
dach_length = [75, 77, 83, 81, 73, 99, 72, 83]
dach_height = [24, 29, 19, 32, 21, 22, 19, 34]

# 사모예드
samo_length = [76, 78, 82, 88, 76, 83, 81, 89]
samo_height = [55, 58, 53, 54, 61, 52, 57, 64]

# 말티즈
mal_length = [35, 39, 38, 41, 30, 57, 41, 35]
mal_height = [23, 26, 19, 30, 21, 24, 28, 20]

# 5.1 레이블링
d_data = np.column_stack((dach_length, dach_height))
d_label = np.array([0, 0, 0, 0, 0, 0, 0, 0])

s_data = np.column_stack((samo_length, samo_height))
s_label = np.array([1, 1, 1, 1, 1, 1, 1, 1])

m_data = np.column_stack((mal_length, mal_height))
m_label = np.array([2, 2, 2, 2, 2, 2, 2, 2])

dogs = np.concatenate((d_data, s_data, m_data))
labels = np.concatenate((d_label, s_label, m_label))

dog_classes = {0: '닥스훈트', 1: '사모예드', 2: '말티즈'}

# data 항목
newdata1 = [[58, 30]]
newdata2 = [[80, 26]]
newdata3 = [[80, 41]]
newdata4 = [[75, 55]]

# 결과
print('A 데이터 분류결과')
for k in range(3, 8, 2):
  knn = KNeighborsClassifier(n_neighbors = k)
  knn.fit(dogs, labels)
  y_pred = knn.predict(newdata1)
  print('A [[58, 30]] : n_neighbors가', k, '일 때 :', dog_classes[y_pred[0]])
print('===============================================')

print('B 데이터 분류결과')
for k in range(3, 8, 2):
  knn = KNeighborsClassifier(n_neighbors = k)
  knn.fit(dogs, labels)
  y_pred = knn.predict(newdata2)
  print('B [[58, 30]] : n_neighbors가', k, '일 때 :', dog_classes[y_pred[0]])
print('===============================================')

print('C 데이터 분류결과')
for k in range(3, 8, 2):
  knn = KNeighborsClassifier(n_neighbors = k)
  knn.fit(dogs, labels)
  y_pred = knn.predict(newdata3)
  print('C [[58, 30]] : n_neighbors가', k, '일 때 :', dog_classes[y_pred[0]])
print('===============================================')

print('D 데이터 분류결과')
for k in range(3, 8, 2):
  knn = KNeighborsClassifier(n_neighbors = k)
  knn.fit(dogs, labels)
  y_pred = knn.predict(newdata4)
  print('D [[58, 30]] : n_neighbors가', k, '일 때 :', dog_classes[y_pred[0]])
print('===============================================')
