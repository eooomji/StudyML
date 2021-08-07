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
# d_label = np.zeros(len(d_data))
d_label = np.array([0, 0, 0, 0, 0, 0, 0, 0])

s_data = np.column_stack((samo_length, samo_height))
# s_label = np.ones(len(s_data))
s_label = np.array([1, 1, 1, 1, 1, 1, 1, 1])

m_data = np.column_stack((mal_length, mal_height))
# m_label = np.array([2., 2., 2., 2., 2., 2., 2.])
m_label = np.array([2, 2, 2, 2, 2, 2, 2, 2])

print('닥스훈트(0) :', d_data)
print('============================')
print('사모예드(1) :', s_data)
print('============================')
print('말티즈(2) :', m_data)
print('============================')
