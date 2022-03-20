#lê ficheiro como lista de linhas sem \n
with open('../dados/lusiadas.txt','r') as f:
    lines = f.read().splitlines()

# cria lista de estrofes
estrofes = []
for i,line in enumerate(lines):
    if line.isnumeric():
        estrofes.append(lines[i+1:i+9])

#print(estrofes)

# imprime estrofes
for estrofe in estrofes:
    for verso in estrofe: print(verso)
    print()

#numero de estrofes
print(len(estrofes))

#numero de versos
numversos = 0
for estrofe in estrofes:
    numversos += len(estrofe)
print(numversos)

#numero de versos (ordem superior)
print(sum(map(len,estrofes)))

def rem_verso(verso):
   for c in verso:
       if not c.isspace() and not c.isalpha():
           verso = verso.replace(c, '')
   return verso

for estrofe in estrofes:
   for i,verso in enumerate(estrofe):
       estrofe[i] = rem_verso(verso)

#escreve estrofes para um ficheiro
with open('estrofes.txt','w') as f:
   for estrofe in estrofes:
       for verso in estrofe:
#            um verso por linha
           f.write(verso+"\n")
#        linha de espaço entre estrofes
       f.write("\n")

# versão imperativa
npalavras = 0
for estrofe in estrofes:
   for verso in estrofe:
       npalavras += len(verso.split())

# versão funcional
def sum_verso(verso):
   return len(verso.split())
def sum_estrofe(estrofe):
   return sum(map(sum_verso,estrofe))
npalavras = sum(map(sum_estrofe,estrofes))

print(npalavras)

import statistics

# versão imperativa
npalavras = []
for estrofe in estrofes:
    npalavras.append(sum_estrofe(estrofe))
avg = statistics.mean(npalavras)

# versão funcional
avg = statistics.mean(map(sum_estrofe,estrofes))

print(avg)