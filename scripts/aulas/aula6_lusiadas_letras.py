# lê estrofes de ficheiro
with open('estrofes.txt','r') as f:
    texto = f.read()

# número de ocorrências por caracter
count = {}
for c in texto:
    if c.isalpha():
        count[c] = 1 + count.get(c,0)

print(count)