import json

with open('targaryen.json','r') as f:
    targaryen = json.load(f)

def geracoes(t):
    if t["children"]:
        return 1 + max([ geracoes(c) for c in t["children"] ])
    else: return 1

print(geracoes(targaryen))

def mulheres(t):
    mulher = t["gender"] == "female"
    return int(mulher) + sum([mulheres(c) for c in t["children"] ])

print(mulheres(targaryen))

def filhosDe(name,t):
    if t["name"] == name: return len(t["children"])
    else:
        for c in t["children"]:
            r = filhosDe(name,c)
            if r: return r
        return None

print(filhosDe("Rhaenyra Targaryen",targaryen))


