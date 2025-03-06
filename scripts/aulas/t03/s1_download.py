import urllib.request
import ssl

context = ssl.create_default_context()
context.check_hostname = False
context.verify_mode = ssl.CERT_NONE

url = 'http://www.gutenberg.org/cache/epub/3333/pg3333.txt'
filename= 'lusiadas.txt'

# se tiverem erros de SSL, para fazer download do ficheiro sem verificação de certificados
with urllib.request.urlopen(url, context=context) as response, open(filename, 'wb') as out_file:
    out_file.write(response.read())

# para fazer download do ficheiro normalmente
#urllib.request.urlretrieve(url,filename,context=context)

with open('lusiadas.txt','r') as f:
    lines = f.readlines()
for line in lines:
    print(line)