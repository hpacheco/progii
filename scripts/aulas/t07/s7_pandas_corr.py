import urllib.request
import pandas as pd
import matplotlib.pyplot as plt
import ssl

context = ssl.create_default_context()
context.check_hostname = False
context.verify_mode = ssl.CERT_NONE

url = 'https://raw.githubusercontent.com/dssg-pt/covid19pt-data/master/data.csv'
filename ='data.csv'

with urllib.request.urlopen(url, context=context) as response, open(filename, 'wb') as out_file:
    out_file.write(response.read())

amostras = pd.read_csv('amostras.csv',index_col='data')
amostras = amostras['amostras_novas']
amostras.fillna(0,inplace=True)

dados = pd.read_csv('data.csv',index_col='data')
confirmados = dados['confirmados_novos']

amostras_confirmados = pd.merge(amostras,confirmados,how='inner',left_index=True,right_index=True)

print(amostras_confirmados.corr())

fig, ax = plt.subplots()
amostras_confirmados[['amostras_novas']].plot(ax=ax)
amostras_confirmados[['confirmados_novos']].plot(ax=ax,secondary_y=True)
plt.show()
