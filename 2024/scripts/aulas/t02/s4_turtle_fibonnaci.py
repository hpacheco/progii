import turtle
import math

window = turtle.Screen(); alex = turtle.Turtle()

prev = 0 # fib(n-1)
fib  = 1 # fib(n)

# vamos aproximar um quarto de círculo com um polígono
# número de vértices do polígono
n = 360

alex.right(90)
while True:
    fator = 10 # apenas para redimensionar a visualização
    # lado = 2 * sen(pi / n) * r
    arc = 2 * math.sin(math.pi / n) * (fib * fator)
    for j in range(90):
        alex.forward(arc)
        alex.left(1)
    # calcula o próximo número de fibonnaci
    fib,prev = fib + prev,fib