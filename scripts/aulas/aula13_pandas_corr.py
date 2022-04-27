import pandas as pd
import matplotlib.pyplot as plt

amostras = pd.read_csv('../../dados/amostras.csv',index_col='data')
amostras = amostras['amostras_novas']
amostras.fillna(0,inplace=True)

dados = pd.read_csv('../../dados/data.csv',index_col='data')
confirmados = dados['confirmados_novos']

amostras_confirmados = pd.merge(amostras,confirmados,how='inner',left_index=True,right_index=True)

print(amostras_confirmados.corr())

fig, ax = plt.subplots()
amostras_confirmados[['amostras_novas']].plot(ax=ax)
amostras_confirmados[['confirmados_novos']].plot(ax=ax,secondary_y=True)
plt.show()
