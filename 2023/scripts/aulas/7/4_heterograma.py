
import unidecode as uni

def normaliza(c):
    return (uni.unidecode(c.lower()))

def alpha(c): return c.isalpha()
def heterograma(frase):
    chars = list(filter(alpha,normaliza(frase)))
    return len(set(chars)) == len(chars)

print(heterograma("The big dwarf only jumps."))