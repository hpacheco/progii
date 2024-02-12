import re

r = re.compile("[o|O].[a|A]")
print(r.search("OlA"))
# <re.Match object; span=(0, 3), match='OlA'>
m = r.search("socapa")
print(m.start(),m.end(),m.group())
# 1 4 oca

r = re.compile("abc(.+)")
print(r.fullmatch("abcdef"))
# <re.Match object; span=(0, 6), match='abcdef'>
print(r.fullmatch("abc"))
# None

r = re.compile("[A-z].[A-z]")
print(r.findall("Eu gosto de Python"))
# ['u g', 'ost', 'o d', 'e P', 'yth']

import regex as re

r = re.compile("[A-z].[A-z]")
print(r.findall("Eu gosto de Python",overlapped=True))
# ['u g', 'gos', 'ost', 'sto', 'o d', 'e P', 'Pyt', 'yth', 'tho', 'hon']

for m in r.finditer("asdasdasd"):
    print(m)
# <regex.Match object; span=(0, 3), match='asd'>
# <regex.Match object; span=(3, 6), match='asd'>
# <regex.Match object; span=(6, 9), match='asd'>