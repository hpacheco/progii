import pandas as pd
import matplotlib.pyplot as plt

vacinas = pd.read_csv('../../dados/vacinas.csv',index_col='data')
vacinas = vacinas[[col for col in vacinas.columns if col.startswith('doses')]]
vacinas = vacinas.dropna()

vacinas.plot()
plt.show()