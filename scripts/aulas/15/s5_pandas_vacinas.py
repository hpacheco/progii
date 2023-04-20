import urllib.request
import pandas as pd
import matplotlib.pyplot as plt

url = 'https://raw.githubusercontent.com/dssg-pt/covid19pt-data/master/vacinas.csv'
urllib.request.urlretrieve(url,'vacinas.csv')

vacinas = pd.read_csv('vacinas.csv',index_col='data')
vacinas = vacinas[[col for col in vacinas.columns if col.startswith('doses')]]
vacinas = vacinas.dropna()

vacinas.plot()
plt.show()