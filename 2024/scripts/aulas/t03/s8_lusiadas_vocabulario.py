import unidecode as uni

# apaga acentos e capitalização
def normaliza(c):
    return (uni.unidecode(c.lower()))

# lê estrofes de ficheiro
with open('estrofes.txt','r') as f:
    texto = f.read()

# set de palavras
vocabulario = set(normaliza(texto).split())

print(vocabulario)
