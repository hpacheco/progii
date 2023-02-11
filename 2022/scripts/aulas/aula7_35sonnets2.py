from aula7_35sonnets import *

# normaliza string
def trim(str):
    for c in str:
        if not c.isalpha():
            str = str.replace(c,'')
    return str.lower()

# conta palavras
def conta(str):
    palavras = [ trim(p) for p in str.split()]
    count = {}
    for p in palavras:
        count[p] = 1 + count.get(p,0)
    return count

palavras_por_poema = { i:conta(p) for i,p in poemas.items() }

print(palavras_por_poema)
