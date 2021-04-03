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

screen.blit(background,(0,0))
draw_ellipse(30000,60000,red)
pygame.display.update()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: running=False
