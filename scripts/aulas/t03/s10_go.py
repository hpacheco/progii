import urllib.request
import ssl

context = ssl.create_default_context()
context.check_hostname = False
context.verify_mode = ssl.CERT_NONE


url = 'https://github.com/osuoer/computational-biology/blob/master/PZ.annot.txt?raw=true'
filename = 'PZ.annot.txt'

# se tiverem erros de SSL, para fazer download do ficheiro sem verificação de certificados
with urllib.request.urlopen(url, context=context) as response, open(filename, 'wb') as out_file:
    out_file.write(response.read())

# para fazer download do ficheiro normalmente
#urllib.request.urlretrieve(url,filename)

with open('PZ.annot.txt','r') as f:
    linhas = f.read().splitlines()

genes = {}
for linha in linhas:
    id,go,name = linha.split('\t')
    genes[name] = genes.get(name,set()) | {id,go}

# gene com mais identificadores
maxg = max(genes,key=lambda g: len(genes[g]))
print(maxg,genes[maxg])