
def leTexto(ficheiro):
    return None

sermaoLinhas = leTexto('dados/sermao.txt')

def separaLinha(linha):
    return None

def separaLinhas(lista):
    return None

def organizaCapitulos(lista):
    return None

def organizaSermao(linhas):
    lista = separaLinhas(linhas)
    titulo = separaLinha(lista[0][0])
    descricao = list(map(separaLinha,lista[1]))
    return (titulo,descricao,organizaCapitulos(lista[2:]))

sermaoOrganizado = organizaSermao(sermaoLinhas)

def totais(sermao):
  return None

def deusPeixes(sermao):
  return None

def maiorParagrafo(sermao):
  return None

la_dic = set(leTexto('dados/la.txt'))
pt_dic = set(leTexto('dados/pt.txt'))

def spellcheck(palavra):
    if palavra in pt_dic: return 1
    if palavra in la_dic: return 2
    return 0

def normalizaPalavra(palavra):
    return None

def formataPalavra(palavra):
    return None

def formataSermao(sermao):
    return None

with open('sermao.md','w') as f:
  f.write(formataSermao(sermaoOrganizado))
