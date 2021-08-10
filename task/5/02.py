from sklearn.metrics import confusion_matrix

dogs = np.concatenate((d_data, s_data, m_data))
labels = np.concatenate((d_label, s_label, m_label))

dog_classes = {0: '닥스훈트', 1: '사모예드', 2: '말티즈'}

k = 3
knn = KNeighborsClassifier(n_neighbors = k)
knn.fit(dogs, labels)
y_pred_all = knn.predict(dogs)

conf_mat = confusion_matrix(labels, y_pred_all)
conf_mat
