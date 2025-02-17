import urllib.request

url = 'http://www.gutenberg.org/cache/epub/3333/pg3333.txt'
urllib.request.urlretrieve(url,'lusiadas.txt')

with open('lusiadas.txt','r') as f:
    lines = f.readlines()
for line in lines:
    print(line)