newdata_length = [58, 80, 80, 75]
newdata_height = [30, 26, 41, 55]

dog_length = np.array(dach_length + samo_length + mal_length + newdata_length)
dog_height = np.array(dach_height + samo_height + mal_height + newdata_height)

dog_data = np.column_stack((dog_length, dog_height))

plt.title("Dog data without label")
plt.scatter(dog_length, dog_height)

# 5.6 k-평균 알고리즘 적용
def kmeans_predict_plot(X, k):
  model = cluster.KMeans(n_clusters=k)
  model.fit(X)
  labels = model.predict(X)
  colors = np.array(['red', 'green', 'blue', 'magenta'])
  plt.suptitle('k-Means clustering, k={}'.format(k))
  plt.scatter(X[:, 0], X[:, 1], color=colors[labels])
  
# 그래프 그리기
kmeans_predict_plot(dog_data, k=2)
kmeans_predict_plot(dog_data, k=3)
kmeans_predict_plot(dog_data, k=4)
