import urllib.request

url = 'http://www.gutenberg.org/cache/epub/3333/pg3333.txt'
urllib.request.urlretrieve(url,'../dados/lusiadas.txt')

with open('../dados/lusiadas.txt','r') as f:
    lines = f.readlines()
for line in lines:
    print(line)