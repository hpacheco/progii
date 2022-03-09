import turtle

window = turtle.Screen()
window.bgcolor("lightgreen")
window.title("Hello, Alex!")

alex = turtle.Turtle()
alex.color("blue")
alex.pensize(3)

for _ in range(4):
    alex.forward(100)
    alex.left(90)

window.mainloop()
