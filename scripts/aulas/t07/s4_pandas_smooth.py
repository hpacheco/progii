from s3_pandas_novas import *
import matplotlib.pyplot as plt

smooth = novas_amostras.copy()
for i in range(len(smooth)) :
    smooth.iloc[i] = novas_amostras.iloc[i-30:i+30].mean()

smooth.plot()
plt.show()





