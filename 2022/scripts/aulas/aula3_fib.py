import turtle
import math

window = turtle.Screen(); alex = turtle.Turtle()

prev = 0 # fib(n-1)
fib  = 1 # fib(n)

alex.right(90)
while True:
    arc = math.pi * fib / 10
    for j in range(90):
        alex.forward(arc)
        alex.left(1)
    fib,prev = fib + prev,fib
