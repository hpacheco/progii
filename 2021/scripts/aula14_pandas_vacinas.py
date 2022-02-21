import pandas as pd
import matplotlib.pyplot as plt

vacinas = pd.read_csv('../dados/vacinas.csv',index_col='data')
vacinas = vacinas.dropna()

vacinas.plot()
plt.show()