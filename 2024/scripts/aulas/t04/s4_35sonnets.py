from s3_35sonnets import *
import matplotlib.pyplot as plt

palavras_total = sorted(palavras_total.items(),key=lambda kv: kv[1])
mais_frequentes = dict(palavras_total[-10:])

plt.bar(mais_frequentes.keys(), mais_frequentes.values())
plt.show()