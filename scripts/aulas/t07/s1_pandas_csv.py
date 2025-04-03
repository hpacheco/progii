import urllib.request
import pandas as pd
import ssl

context = ssl.create_default_context()
context.check_hostname = False
context.verify_mode = ssl.CERT_NONE

url = 'https://raw.githubusercontent.com/dssg-pt/covid19pt-data/master/amostras.csv'
filename = 'amostras.csv'

#with urllib.request.urlopen(url, context=context) as response, open(filename, 'wb') as out_file:
#    out_file.write(response.read())

amostras = pd.read_csv('amostras.csv',index_col='data')
amostras.fillna(0,inplace=True)
print(amostras)
print(amostras.info())

