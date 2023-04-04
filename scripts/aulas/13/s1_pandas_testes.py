import pandas as pd
import matplotlib.pyplot as plt

amostras = pd.read_csv('../12/amostras.csv',index_col='data')
amostras.fillna(0,inplace=True)

novas_colunas = [c for c in amostras.columns if c.endswith('_novas')]
novas_amostras = amostras[novas_colunas]

# converte datas textuais para datetime
# formato de data explícito para evitar que o pandas troque dias com meses
novas = novas_amostras.rename(lambda str : pd.to_datetime(str,format='%d-%m-%Y'))

print(novas)
print(novas.info())

# adicionar duas novas colunas para mês e ano
novas['month'] = novas.index.month
novas['year'] = novas.index.year

# agrupar linhas por (mês,ano)
meses = novas.groupby(['month','year']).mean()
# ordenar por data crescente (podíamos agrupar por (ano,mês) para evitar a ordenação)
meses.sort_values(by=['year','month'], inplace=True)
print(meses)

meses.plot(kind='bar')
plt.tight_layout()
plt.show()


