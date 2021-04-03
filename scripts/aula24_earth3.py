import math
import pygame

red = (180,50,50)
green = (50,180,50)
yellow = (255, 255, 0)
orange = (255, 128, 0)
blue = (50, 50, 180)
black=(0,0,0)

proportion = 200
earthRadius = 6371
EarthRadius = earthRadius / proportion

background = pygame.image.load('../dados/space.png')
earth = pygame.image.load('../dados/earth.png')
screenX,screenY = background.get_size()
pygame.display.set_icon(earth)
screen = pygame.display.set_mode((screenX,screenY))
Center = (screenX/2,screenY/2)

running = True

# make background
EarthWidth = int(EarthRadius * 2)
earth = pygame.transform.smoothscale(earth, (EarthWidth, EarthWidth))
earthRect = earth.get_rect()
earthRect.center = Center
background.blit(earth, earthRect)

def draw_ellipse_point(perigee,apogee,color,theta):

    a = (perigee + apogee) / 2
    c = (apogee - perigee) / 2
    C = c / proportion
    b = math.sqrt(a ** 2 - c ** 2)
    y = b * math.sin(theta)
    x = a * math.cos(theta)

    X = x / proportion
    Y = y / proportion
    Pos = (Center[0] + C + X,Center[1] + Y)
    pygame.draw.circle(screen,color,Pos,1)

def draw_ellipse(perigee,apogee,color):
    for ang in range(0,360):
        draw_ellipse_point(perigee,apogee,color,math.radians(ang))

screen.blit(background,(0,0))
draw_ellipse(30000,60000,red)
pygame.display.update()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: running=False
