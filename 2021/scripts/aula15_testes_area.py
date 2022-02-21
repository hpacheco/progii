import pandas as pd
import matplotlib.pyplot as plt

amostras = pd.read_csv('../dados/amostras.csv')
amostras.dropna(inplace=True)

amostras['pcr'] = amostras['amostras_pcr'] / amostras['amostras']
amostras['antigenio'] = amostras['amostras_antigenio'] / amostras['amostras']
amostras[['pcr','antigenio']].plot(kind='area',stacked=True)

plt.tick_params(axis='x',bottom=False,labelbottom=False)
plt.ylim(0.9,1)
plt.yticks([0.9,0.95,1],["90%","95%","100%"])
plt.show()