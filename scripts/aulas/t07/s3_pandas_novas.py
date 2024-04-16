from s1_pandas_csv import *
import matplotlib.pyplot as plt

novas_colunas = [c for c in amostras.columns if c.endswith('_novas')]
novas_amostras = amostras[novas_colunas]
#print(novas_amostras)

novas_amostras.plot()
plt.show()

