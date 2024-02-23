import unidecode as uni
import matplotlib.pyplot as plt

# lê estrofes de ficheiro
with open('estrofes.txt','r') as f:
    texto = f.read()

def normaliza(c):
    return (uni.unidecode(c.lower()))

# número de ocorrências por caracter, sem acentos e e capitalização
count = {}
for c in texto:
    if c.isalpha():
        c = normaliza(c)
        count[c] = 1 + count.get(c,0)
print(count)

plt.bar(count.keys(), count.values())
plt.show()