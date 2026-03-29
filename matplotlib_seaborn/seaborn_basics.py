import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

data = np.random.rand(6,6)
sns.heatmap(data, annot=True, cmap="coolwarm")
plt.title("Heat map using Seaborn")
plt.show()
