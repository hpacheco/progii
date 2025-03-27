import numpy as np
import matplotlib.pyplot as plt

a = np.array([[1,1.5,3],[4,5,5]])
hist,bins = np.histogram(a,bins=range(6))

plt.hist(bins[:-1], bins, weights=hist)
plt.show()
