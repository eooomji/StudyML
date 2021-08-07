import numpy as np
from sklearn.neighbors import KNeighborsClassifier

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
  print('B [[80, 26]] : n_neighbors가', k, '일 때 :', dog_classes[y_pred[0]])
print('===============================================')

print('C 데이터 분류결과')
for k in range(3, 8, 2):
  knn = KNeighborsClassifier(n_neighbors = k)
  knn.fit(dogs, labels)
  y_pred = knn.predict(newdata3)
  print('C [[80, 41]] : n_neighbors가', k, '일 때 :', dog_classes[y_pred[0]])
print('===============================================')

print('D 데이터 분류결과')
for k in range(3, 8, 2):
  knn = KNeighborsClassifier(n_neighbors = k)
  knn.fit(dogs, labels)
  y_pred = knn.predict(newdata4)
  print('D [[75, 55]] : n_neighbors가', k, '일 때 :', dog_classes[y_pred[0]])
print('===============================================')
