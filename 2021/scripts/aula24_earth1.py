import pygame
import math

red = (180,50,50)
green = (50,180,50)
yellow = (255, 255, 0)
orange = (255, 128, 0)
blue = (50, 50, 180)
black=(0,0,0)

proportion = 200
earthRadius = 6371
EarthRadius = earthRadius / proportion

screen = pygame.display.set_mode((1024,640))
Center = (1024/2,640/2)

running = True

def draw_ellipse(perigee,apogee,color):

    Perigee = perigee / proportion
    Apogee = apogee / proportion

    a = (perigee + apogee) / 2
    c = (apogee - perigee) / 2
    b = math.sqrt(a**2 - c**2)

    A = a / proportion
    B = b / proportion
    C = c / proportion

    pygame.draw.ellipse(screen,color,(Center[0]-Perigee,Center[1]-B,2*A,2*B),width=1)

pygame.draw.circle(screen,green,Center,EarthRadius)
draw_ellipse(30000,60000,red)
pygame.display.update()

while running:
    screen.fill(black)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: running=False
