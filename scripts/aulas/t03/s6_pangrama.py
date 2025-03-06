
import unidecode as uni

def normaliza(c):
    return (uni.unidecode(c.lower()))

def pangrama(frase):
    alfabeto = set("abcdefghijklmnopqrstuvwxyz")
    chars = set(normaliza(frase))
    return alfabeto.issubset(chars)

print(pangrama("Fidel exporta whiskey, vinho, queijo azul, caju, manga e nabo."))