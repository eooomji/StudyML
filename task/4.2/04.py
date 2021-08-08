import matplotlib.pyplot as plt
import seaborn as sns

sns.set(rc={'figure.figsize':(5,3)})
correlation_matrix = PCC.corr().round(2)
sns.heatmap(data=correlation_matrix, annot=True)
plt.show()
