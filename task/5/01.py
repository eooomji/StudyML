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
