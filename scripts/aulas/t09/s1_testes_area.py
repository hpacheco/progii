import pandas as pd
import matplotlib.pyplot as plt

amostras = pd.read_csv('../t07/amostras.csv')
amostras.dropna(inplace=True)

amostras['pcr'] = amostras['amostras_pcr'] / amostras['amostras']
amostras['antigenio'] = amostras['amostras_antigenio'] / amostras['amostras']
amostras[['pcr','antigenio']].plot(kind='area',stacked=True)

plt.tick_params(axis='x',bottom=False,labelbottom=False)
plt.ylim(0.4,1)
plt.yticks([0.4,0.5,0.6,0.7,0.8,0.9,1],["40%","50%","60%","70%","80%","90%","100%"])
plt.show()