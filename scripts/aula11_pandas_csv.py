import pandas as pd
import matplotlib.pyplot as plt

amostras = pd.read_csv('../dados/amostras.csv',index_col='data')
amostras.fillna(0,inplace=True)
#print(amostras)
#print(amostras.info())

#amostras.plot()
#plt.show()

novas_colunas = [c for c in amostras.columns if c.endswith('_novas')]
novas_amostras = amostras[novas_colunas]
print(novas_amostras)
#novas_amostras.plot()
#plt.show()

smooth = novas_amostras.copy()
for i in range(len(smooth)) :
    smooth.iloc[i] = novas_amostras.iloc[i-3:i+3].mean()
#smooth.plot()
#plt.show()

#1º dia antigenio
primeiro_anti = amostras[amostras['amostras_antigenio'] > 0].index[0]
print(primeiro_anti)
#
# dias e valores dos máximos de novas amostras por categoria
max_datas = novas_amostras.idxmax()
print(max_datas)
max_categorias = { k : (data,novas_amostras[k][data]) for k,data in dict(max_datas).items() }
print(max_categorias)

# # dias de Dezembro acima da média de novas amostras
novas = novas_amostras.rename(lambda str : pd.to_datetime(str))
print(novas.info())
means = novas.mean()
print(means)

above_mean = (novas['amostras_novas'] >= means['amostras_novas'])
dec_above_mean = novas[above_mean & (novas.index.month == 12)]
print(dec_above_mean)



