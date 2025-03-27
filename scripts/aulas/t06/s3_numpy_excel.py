import urllib.request
import pandas as pd
import numpy as np
import ssl

context = ssl.create_default_context()
context.check_hostname = False
context.verify_mode = ssl.CERT_NONE

url = 'https://api.ipma.pt/open-data/observation/climate/monthly-long-series/PT100-tx-tn-prec.xlsx'
filename = 'PT100-tx-tn-prec.xlsx'

with urllib.request.urlopen(url, context=context) as response, open(filename, 'wb') as out_file:
    out_file.write(response.read())

dados = pd.read_excel('PT100-tx-tn-prec.xlsx',sheet_name=3).to_numpy()
print(dados)
print(dados.shape)
linhas,colunas = dados.shape

anual = dados[:linhas-1,[0,colunas-1]]
print(anual)

# anos menos e mais chuvoso
min_prec = anual[:,1].min()
print(min_prec)
max_prec = anual[:,1].max()
print(max_prec)

print(anual[anual[:,1] == min_prec])
print(anual[anual[:,1] == max_prec])

# média de precipitação Sec. XX
xx = anual[anual[:,0] < 2000]
#print(xx)
xx_prec = np.mean(xx[:,1])
print(xx_prec)

# média de precipitação Sec. XXI
xxi = anual[anual[:,0] >= 2000]
xxi_prec = np.mean(xxi[:,1])
print(xxi_prec)




