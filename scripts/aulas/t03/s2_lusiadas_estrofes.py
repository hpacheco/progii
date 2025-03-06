#lê ficheiro como lista de linhas sem \n
with open('lusiadas.txt','r') as f:
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

# remove caracteres não espaço nem alfanuméricos num verso
def rem_verso(verso):
   for c in verso:
       if not c.isspace() and not (c.isalpha() or c.isalnum()):
           verso = verso.replace(c, '')
   return verso

import re

# remove espaços e caracteres não alfabéticos num verso (expressões regulares)
# \S: qualquer caracter não de espaçamento
# \W: qualquer caracter não alfanumérico
def rem_verso2(verso):
    return re.sub("(\S|\W)","",verso)

# remove caracteres especiais em cada verso das estrofes
# modificar listas in-place, cópia de strings
for estrofe in estrofes:
   for i,verso in enumerate(estrofe):
       estrofe[i] = rem_verso(verso)

# remove caracteres especiais em cada verso das estrofes
# ordem superior
rem_versos = lambda versos : list(map(rem_verso,versos))
estrofes2 = list(map(rem_versos,estrofes))
#print(estrofes2)

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