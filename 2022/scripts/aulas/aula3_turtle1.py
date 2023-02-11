import turtle

window = turtle.Screen()
window.bgcolor("lightgreen")
window.title("Hello, Alex!")

alex = turtle.Turtle()
alex.color("blue")
alex.pensize(3)

alex.forward(50)
alex.left(120)
alex.forward(50)

window.mainloop()
