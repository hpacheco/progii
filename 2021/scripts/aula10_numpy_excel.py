import pandas as pd
import numpy as np

dados = pd.read_excel('../dados/PT100-tx-tn-prec.xlsx',sheet_name=3).to_numpy()
print(dados)
print(dados.shape)

anual = dados[:89,[0,17]]
print(anual)

min_prec = anual[:,1].min()
print(min_prec)
max_prec = anual[:,1].max()

print(anual[anual[:,1] == min_prec])
print(anual[anual[:,1] == max_prec])

xx = anual[anual[:,0] < 2000]
print(xx)
xx_prec = np.mean(xx[:,1])
print(xx_prec)

xxi = anual[anual[:,0] >= 2000]
xxi_prec = np.mean(xxi[:,1])
print(xxi_prec)




