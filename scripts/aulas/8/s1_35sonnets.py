import urllib.request
url = 'http://www.gutenberg.org/files/19978/19978-0.txt'
#urllib.request.urlretrieve(url,'../../../dados/35sonnets.txt')
with open('../../../dados/35sonnets.txt','r') as f: ls = f.read().splitlines()

# testa se linha é numeração romana
def roman(s):
    s = s[:-1] #deixa cair último caracter
    bad = { c for c in s if not c.isupper() }
    return len(s) > 0 and len(bad) == 0

# extrai poema
def poem(lines):
    res = []
    for l in lines:
        if len(l) == 0: break
        else: res.append(l)
    return "\n".join(res)

poemas = { l[:-1] : poem(ls[i+3:]) for i,l in enumerate(ls) if roman(l) }

print(poemas)