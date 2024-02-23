from s1_35sonnets import *

# normaliza string
def trim(s):
    return "".join([c.lower() for c in s if c.isalpha()])

# conta palavras
def conta(s):
    palavras = [ trim(p) for p in s.split()]
    count = {}
    for p in palavras:
        count[p] = 1 + count.get(p,0)
    return count

palavras_por_poema = { i:conta(p) for i,p in poemas.items() }

print(palavras_por_poema)
