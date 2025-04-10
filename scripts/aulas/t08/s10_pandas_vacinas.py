import urllib.request
import pandas as pd
import matplotlib.pyplot as plt
import ssl

context = ssl.create_default_context()
context.check_hostname = False
context.verify_mode = ssl.CERT_NONE

url = 'https://raw.githubusercontent.com/dssg-pt/covid19pt-data/master/vacinas.csv'
filename = 'vacinas.csv'

with urllib.request.urlopen(url, context=context) as response, open(filename, 'wb') as out_file:
    out_file.write(response.read())

vacinas = pd.read_csv('vacinas.csv',index_col='data')
vacinas = vacinas[[col for col in vacinas.columns if col.startswith('doses')]]
vacinas = vacinas.dropna()

vacinas.plot()
plt.show()
#plt.savefig("vacinas.jpg")