import re
from unidecode import unidecode # para eliminar acentos

with open('estrofes.txt','r') as f:
    palavras = f.read().split()

def encontraPalavras(regexp,normalize=False):
    s = set()
    for palavra in palavras:
        r = re.compile(regexp)
        # quando normaliza, ignora acentos e capitalização
        p = unidecode(palavra).lower() if normalize else palavra
        # match com a palavra toda
        m = r.fullmatch(p)
        if m: s.add(palavra)
    return s

#palavras começadas por "a", comprimento entre 4 e 6
print(encontraPalavras("a.{3,5}"))

#palavras acabadas em "aõ" ou em "ões"
print(encontraPalavras(".*(ão|ões)$"))

#palavras começadas em "ra" e acabadas em "os"
print(encontraPalavras("^ra.*os$"))

#palavras que usam uma vogal (sem considerar acentos)
print(encontraPalavras("[^aeiou]*[aeiou][^aeiou]*",True))

#palavras que usam no máximo duas vogais (sem considerar acentos)
print(encontraPalavras("[^aeiou]*([aeiou][^aeiou]*){0,2}",normalize=True))
