
import numpy as np
import matplotlib.pyplot as plt

a = np.array([[1,1.5,3],[4,5,5]])
hist,bins = np.histogram(a,bins=range(6))
print(hist)
# [0 2 0 1 3]
print(bins)
# [0 1 2 3 4 5]

# desenhar o histograma com o matplotlib (vamos ver mais à frente)
plt.hist(a.reshape(6),bins=range(6))
plt.show()

