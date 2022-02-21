# Projeto 0 - Desenferrujar

Nas primeiras aulas vamos reavivar os nossos conhecimentos fundamentais de programação em Python: cálculo numérico, listas, iteração e processamento de strings.

Crie um novo ficheiro projeto0.py para desenvolver o projeto e abra-o com um IDE à sua escolha.

Neste projeto (primeiras duas semanas de aulas práticas) vamos resolver livremente alguns exercícios lecionados em edições anteriores da cadeira anterior de Programação I. Sinta-se à vontade para requisitar mais ou novos exercícios aos docentes.

Este projeto é completamente livre e não sujeito a avaliação. Os alunos devem sentir-se à vontade para explorar exercícios de diferentes tipos, resolver exercícios em conjunto, discutir soluções com a turma ou pedir sugestões aos docentes.

## Cálculo numérico

### Exercício 1.1

Escreva uma função ``perim_circ(r)`` que calcule o perímetro de um círculo com raio `r`.
Por exemplo:
```
> perim_circ(4)
25.132741228718345
```
<details>
<summary>Solução</summary>
    
```python
def perim_circ(r):
    return 2 * math.pi * r
```
</details>

### Exercício 1.2

Escreva uma função `area_circ(r)` que calcule a área de um círculo com raio `rª .
Por exemplo:
```
> area_circ(4)
50.26548245743669
```

<details>
<summary>Solução</summary>
    
```python
def area_circ(r):
    return math.pi * r**2
```
</details>

### Exercício 1.3

A conversão entre medidas de temperatura em *Fahrenheit* e *Celsius* pode ser efectuada pela fórmula

$$
C = \frac{5}{9} (F - 32)
$$

onde `F` é a temperatura em *Fahrenheit* e `C` em *Celsius*. Escreva uma função `celsius(F)` que efetue a
conversão de *Fahrenheit* para *Celsius* de uma temperatura `F`.
Por exemplo:
```
> celsius(0)
-17.77777777777778
> celsius(20)
-6.666666666666667
```
<details>
<summary>Solução</summary>

```python
def celsius(F):
    return (5/9) * (F - 32)
```
</details>

### Exercício 1.4

A distância entre dois pontos no plano de coordenadas $(x_1,y_1)$ e $(x_2,y_2)$ é dada por:
$$ d = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2} $$
Implemente uma função dist($x_1$,$y_1$,$x_2$,$y_2$) que use esta fórmula para calcular a distância.

```python
def dist(x1,y1,x2,y2):
    return math.sqrt((x2-x1)**2 + (y2-y1)**2)
dist(1,1,4,4)
```

### Exercício 1.5

Escreva uma função `radianos(graus,mins,segs)` que, dado o valor de um ângulo em graus,
minutos e segundos, converte-o para radianos. Relembre que $360º$
corresponde a $2 \pi$ radianos, cada grau
tem 60 minutos e cada minuto tem 60 segundos.

```python
def radianos(graus,mins,segs):
    mins = mins + segs / 60
    graus = graus + mins / 60
    return graus * (2 * math.pi / 360)
print(radianos(0,0,60))
print(radianos(0,60,0))
print(radianos(180,10,40))
````

## Exercício 1.6

Escreva uma função `segundos(horas,mins,segs)` que, dada uma duração em horas, minutos e segundos, calcula e retorna essa mesma duração em segundos.

```python
def segundos(horas,mins,segs):
    mins = mins + horas * 60
    segs = segs + mins * 60
    return segs
print(segundos(2,15,30))
```

# Listas e iteração

## Exercício 2.1

Considere um programa que começa com a atribuição de uma lista de valores de temperatura (em
Celsius) à variável `tempC`:
```python
tempC = [-5,0,5,10,15,20,25]
```

* Escreva um ciclo `for` que imprime cada um dos valores da lista `tempC` numa linha separada.
```python
def tempC1():
    for temp in tempC:
        print(temp)
``

* Imprima os mesmos valores, gerando-os com a função `range`.
```python
def tempC2():
    for temp in range(-5,30,5):
        print(temp)
```

* Escreva um ciclo `while` que produza o mesmo resultado da alínea anterior.
```python
def tempC3():
    temp = -5
    while (temp <= 25):
        print(temp)
        temp += 5
```

* Escreva um ciclo em que para os valores de temperatura acima, em cada linha imprime o valor em Celsius e o valor correspondente em Fahrenheit.
```python
def fahrenheit(c):
    return c * (9/5) + 32
def tempC4():
    for temp in tempC:
        print(temp,fahrenheit(temp))
````

## Exercício 2.2

Considere um programa que começa com a seguinte atribuição:

```python
xs = [12, 10, 32, 3, 66, 17, 42, 99, 20]
```

* Escreva um ciclo `for` que imprime cada um dos números da lista xs numa linha separada.

for x in xs:
    print(x)
    
* Escreva um outro ciclo em que, em cada linha, imprime o número, o seu quadrado, e a sua raiz quadrada.

for x in xs:
    print(x,x**2,math.sqrt(x))
    
* Escreva um ciclo que soma todos os números em xs usando uma variável auxiliar total, e imprime numa linha separada cada um dos números da lista e a soma parcial até esse número.

total = 0
for x in xs:
    print(x,total)
    total += x
    
## Exercício 8

Usando o módulo `turtle`, escreva uma função poligono_reg(t,n,lado), sem valor de retorno,
que faz uma tartaruga t desenhar um polígono regular com n lados de comprimento lado. Por exemplo,
com poligono_reg(t, 3, 100) a tartaruga t desenha um triângulo equilátero com 100 pixels de lado.

Nota: a soma dos ângulos externos de um polígono é $360°$

def poligono_reg(t,n,lado):
    deg = 360 / n
    for _ in range(n):
        t.forward(lado)
        t.right(deg)

window = turtle.Screen()
alex = turtle.Turtle()
poligono_reg(alex,3,100)
window.mainloop()

## Exercício 9

Usando o módulo turtle, escreva uma função friso(t, n, lado), sem valor de retorno, que desenha um friso em forma de muralha com n ameias em que a largura de cada segmento é lado. Por exemplo: com friso(t, 3, 50) uma tartaruga t produz o desenho da figura seguinte.

Note que a tartaruga deve terminar com a orientação original

def friso(t,n,lado):
    t.right(90)
    for _ in range(n):
        t.forward(lado)
        t.left(90)
        t.forward(lado)
        t.right(90)
        t.forward(lado)
        t.right(90)
        t.forward(lado)
        t.left(90)
        
window = turtle.Screen()
alex = turtle.Turtle()
friso(alex,3,100)
window.mainloop()

## Exercício 10

O preço atual da gasolina é 1.63 euros por litro. Implemente a função valor(v) que, dada a lista
v de litros abastecidos numa viagem, retorna o valor total despendido.
Por exemplo, o resultado de `valor([24.8, 49.1])` é 120.457.

def valor(v):
    total = 0
    for litro in v:
        total += litro * 1.63
    return total
valor([24.8, 49.1])

def valor_funcional(v):
    return sum(map(lambda litro : litro * 1.63,v))
valor_funcional([24.8, 49.1])

## Processamento de strings

## Exercício 11

Escreva uma função classifica(p) que, dada a pontuação p obtida num exame (de 0 a 100), retorna
uma mensagem de classificação de acordo com a tabela seguinte. Utilize essa função para escrever um
programa que imprime o número, nome e classificação segundo essa tabela da lista de alunos que se segue
(cada tuplo contém o número de aluno, o seu nome, e a classificação de 0 a 100).

|   pontuação               |  mensagem      | 
|:-------------------------:|:--------------:|
| $$< 0 \,\vee > 100$$      | "inválido"     |
| $$< 50$$                  | "insuficiente" |
| $$\geq 50 \,\wedge < 70$$ | "suficiente"   |
| $$\geq 70 \,\wedge < 80$$ | "bom"          |
| $$\geq 80 \,\wedge < 90$$ | "muito bom"    |
| $$\geq 90$$               | "excelente"    |

studs = [("UP194187304", "José Fonseca", 97),\
         ("UP194209183", "Manuel Ferreira", 87),\
         ("UP194294793", "Maria Ramos", 50),\
         ("UP194399128", "Antonio Fernandes", 45),\
         ("UP194739873", "Júlia Pinto", -1),\
         ("UP194739889", "Manuela Faria", 50)]

def converte_nota(n):
    if n < 0 | n > 100: return "inválido"
    elif n < 50: return "insuficiente"
    elif n >=50 and n < 70: return "suficiente"
    elif n >= 70 and n < 80: return "bom"
    elif n >= 80 and n < 90: return "muito bom"
    else: return "excelente"
def classifica(p):
    for numero,nome,nota in studs:
        print(numero,nome,converte_nota(nota))
classifica(studs)

## Exercício 12

A fórmula de Leibniz para aproximar $\pi$ é:
$$ \pi = 4 x (1 - \frac{1}{3} + \frac{1}{5} - \frac{1}{7} + \frac{1}{9} + \dots) = 4 * \sum_{n=0}^{\infty} \frac{(-1)^n}{2 n + 1} $$

Implemente a função leibniz(k) que resulta no somatório dos primeiros k termos desta série. Documente
a sua função com uma docstring.

def leibniz(k):
    """Calcula a fórmula de Leibniz para os primeiros k termos"""
    return 4 * sum([ ((-1)**n / (2 * n + 1)) for n in range(k) ])
leibniz(4)

## Exercício 13

Implemente a função sum_within(x, a, b) que calcula a soma dos valores da lista x que estão
compreendidos entre a e b.
Por exemplo, o resultado de `sum_within([4, 7, 44, 23], 17, 46)` é 67.

def sum_within(x,a,b):
    s = 0
    for n in x:
        if n >= a and n <= b: s+= n
    return s
sum_within([4, 7, 44, 23], 17, 46)

def sum_wihin_compreensao(x,a,b):
    return sum([n  for n in x if n >= a and n <= b ])
sum_wihin_compreensao([4, 7, 44, 23], 17, 46)

## Exercício 6.5

Escreva a função maximo2(xs) que calcula o segundo maior valor numa lista xs. Verifique que o procedimento retorna o valor correcto quando o maior valor ocorre mais do que uma vez.

Nota: Ignore a palavra distinto no enunciado original.

Exemplos:
```
>>> maximo2([3, -2, 1, 0, -2, 1])
1
>>> maximo2([1, 3, 2, 3, 0])
2
```

def maximo2(xs):
    m1 = float('-inf')
    m2 = float('-inf')
    for x in xs:
        if x > m1: m1=x
        elif x > m2 and x != m1: m2=x
    return m2
print(maximo2([3, -2, 1, 0, -2, 1]))
print(maximo2([1, 3, 2, 3, 0]))

def maximo2_set(xs):
    non_reps = set(xs)
    non_reps.remove(max(non_reps))
    return max(non_reps)
print(maximo2_set([3, -2, 1, 0, -2, 1]))
print(maximo2_set([1, 3, 2, 3, 0]))

## Exercício 6.7

Escreva uma função repetidos(lista) que testa se há elementos repetidos numa lista; o resultado
deve ser um valor lógico. A sua função deve funcionar com listas de vários tipos (e.g. de números ou
de cadeias de carateres).

Exemplos:

```
>>> repetidos(['ola', 'ole', 'abba', 'ole'])
True
>>> repetidos([3, 2, -5, 0, 1])
False
```

def repetidos(lista):
    vistos = []
    for x in lista:
        if x in vistos: return True
        else: vistos.append(x)
    return False
print(repetidos(['ola', 'ole', 'abba', 'ole']))
print(repetidos([3, 2, -5, 0, 1]))

def repetidos_set(lista):
    return len(lista) != len(set(lista))
print(repetidos_set(['ola', 'ole', 'abba', 'ole']))
print(repetidos_set([3, 2, -5, 0, 1]))

## Exercício 5.1

Escreva duas definições da função conta_letras(txt) que retorna o número de letras (maiúsculas
ou minúsculas) sem acentos da cadeia de caracteres txt; numa das versões compare os carateres de
txt com 'a', 'A', 'z', 'Z' e na outra utilize ``string.letters`` ou ``string.ascii_letters``.

Nota: No exercício original dizia para utilizar apenas ``string.letters``, que pode não existir nas versões mais recentes do Python.

Exemplo:

```
>>> conta_letras('Ola, mundo!')
8
```

def is_letra(c):
    return (c >= 'a' and c <= 'z') or (c >= 'A' and c <= 'Z')
def conta_letras(txt):
    n = 0
    for c in txt:
        if is_letra(c): n+=1
    return n
conta_letras('Ola, mundo!')

def conta_letras_compreensao(txt):
    return len([ c for c in txt if is_letra(c) ])
conta_letras_compreensao('Ola, mundo!')

def is_letra2(c):
    return c.lower() in string.ascii_letters
def conta_letras_compreensao2(txt):
    return len([ c for c in txt if is_letra2(c) ])
conta_letras_compreensao2('Ola, mundo!')

## Exercício 5.3

Escreva uma definição da função filtra_letras(txt) que, dada uma cadeia de caracteres txt,
retorna uma cadeia com apenas as suas letras maiúsculas ou minúsculas.

Exemplo:

```
>>> filtra_letras('Ola!, -- disse ele...')
'Oladisseele'
````

def filtra_letras(txt):
    res = ""
    for c in txt:
        if is_letra(c): res+=c
    return res
filtra_letras('Ola!, -- disse ele...')

def filtra_letras_compreensao(txt):
    return "".join([c for c in txt if is_letra(c) ])
filtra_letras_compreensao('Ola!, -- disse ele...')

## Exercício 5.5

Uma cadeia de carateres é um palíndromo se as sequências obtidas lida da esquerda para a direita
e vice-versa são iguais, independentemente das letras serem maiúsculas ou minúsculas. Exemplo:
"reviveR" é um palíndromo.
Escreva uma definição da função palindromo(txt) que verifica se uma cadeia de caracteres é um
palindromo; o resultado deve ser True ou False.

def palindrono(txt):
    for i in range(len(txt)//2):
        if txt[i].lower() != txt[-i-1].lower(): return False
    return True

print(palindrono("reviveR"))
print(palindrono("aaaa"))
print(palindrono("ola olo"))

## Exercício 5.8

A cifra de Cesar consiste em substituir cada carater alfabético de uma mensagem pelo carater
que está k posições à sua direita, na ordem alfabética. Escreva a função cesar(k,txt) que retorna o
valor cifrado de txt usando a “chave” k.

def cesar(k,txt):
    return "".join([ chr(ord(c)+k) for c in txt ])
cesar(3,"mensagem secreta")

## Exercício 5.11

Escreva a função remove_py_com(txt) que remove comentários de linhas de código Python, i.e.,
os sinais de cardinal # e tudo o que estiver à sua direita. Note que se o cardinal estiver dentro de uma
string não é um comentário (considere apenas as strings delimitadas por aspas (")).

Exemplo:

```
>>> remove_py_com("def f(x): # f function ")
'def f(x): '
```

Sugestão: use ciclos while. Nota: não é necessário usar métodos da classe str.

def remove_py_com(txt):
    stop = False
    isstring = False
    i = 0
    while (not stop and i < len(txt)):
        if txt[i] == '\"': isstring = not isstring
        elif txt[i] == '#' and not isstring: stop=True
        i+=1
    return txt[:i-1]
    
print(remove_py_com("def f(x): # f function "))
print(remove_py_com('def "#" f(x) # comentário'))

## Exercício 6.1

Defina uma função forte(passwd) que verifica se uma palavra-passe, dada pela cadeia de caracteres passwd, é forte. Considera-se que a palavra-passe é forte se tiver 8 caracteres ou mais, e incluir
pelo menos uma letra maiúscula, uma letra minúscula e um algarismo. O resultado deve ser um valor
lógico (True ou False).

```
>>> forte('9EwL56')
False
>>> forte('HXKW1393')
False
>>> forte('ffu4G7Fghjk')
True
```

def forte(passwd):
    maiusculas = { c for c in passwd if c.isupper() }
    minusculas = { c for c in passwd if c.islower() }
    algarismos = { c for c in passwd if c.isdigit() }
    return len(passwd) >= 8 and len(maiusculas) > 0 and len(minusculas) > 0 and len(algarismos) > 0

print(forte('9EwL56'))
print(forte('HXKW1393'))
print(forte('ffu4G7Fghjk'))




