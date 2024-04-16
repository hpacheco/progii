from s3_pandas_novas import *
import matplotlib.pyplot as plt

#print(amostras.describe())

# 1º dia antigénio
primeiro_anti = amostras[amostras['amostras_antigenio'] > 0].index[0]
#print(primeiro_anti)

# dias e valores dos máximos de novas amostras por categoria
max_datas = novas_amostras.idxmax()
#print(max_datas)
max_categorias = { k : (data,novas_amostras[k][data]) for k,data in dict(max_datas).items() }
#print(max_categorias)

# dias de Dezembro de 2021 acima da média de novas amostras de 2021
novas = novas_amostras.rename(lambda str : pd.to_datetime(str,infer_datetime_format=True))
novas2021 = novas [ novas.index.year == 2021 ]
#print(novas2021.info())
means2021 = novas2021.mean()
#print(means2021)

above_mean2021 = (novas2021['amostras_novas'] >= means2021['amostras_novas'])
dec_above_mean2021 = novas2021[above_mean2021 & (novas2021.index.month == 12)]
#print(dec_above_mean2021)