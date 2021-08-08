import matplotlib.pyplot as plt
import seaborn as sns

sns.pairplot(PCC[['horsePower', 'weight', 'efficiency']])
plt.show()
