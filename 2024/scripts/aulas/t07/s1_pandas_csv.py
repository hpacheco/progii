import urllib.request
import pandas as pd

url = 'https://raw.githubusercontent.com/dssg-pt/covid19pt-data/master/amostras.csv'
urllib.request.urlretrieve(url,'amostras.csv')

amostras = pd.read_csv('amostras.csv',index_col='data')
amostras.fillna(0,inplace=True)
print(amostras)
print(amostras.info())

