import turtle

def draw_multicolor_square(animal,size):
    for color in ["red", "purple", "hotpink", "blue"]:
        animal.color(color)
        animal.forward(size)
        animal.left(90)

window = turtle.Screen(); alex = turtle.Turtle()

size = 20
while True:
    draw_multicolor_square(alex,size)
    size += 10
    alex.forward(10)
    alex.right(18)

window.mainloop()