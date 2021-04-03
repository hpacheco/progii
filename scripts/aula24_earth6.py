import math
import pygame
import pandas as pd

data = pd.read_excel('../dados/UCS-Satellite-Database-1-1-2021.xls',usecols=(8,11,12,14))
data.dropna(inplace=True)

red = (180,50,50)
green = (50,180,50)
yellow = (255, 255, 0)
orange = (255, 128, 0)
blue = (50, 50, 180)
black=(0,0,0)

proportion = 100
perspective = 10
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

def rotate_point_around(center,point,degs):
    rads = math.radians(-degs)
    x = point[0] - center[0]
    y = point[1] - center[1]
    x1 = x * math.cos(rads) - y * math.sin(rads)
    y1 = y * math.cos(rads) + x * math.sin(rads)
    return (x1 + center[0],y1 + center[1])

# test collision of a point with Earth's circle
def behind_earth(P,theta):
    Px,Py = P
    Cx,Cy = Center
    Dist = math.sqrt (abs(Px-Cx)**2 + abs(Py-Cy)**2)
    return Dist <= EarthRadius and theta > math.pi

def draw_satellite(perigee,apogee,inclination,color,theta):

    # original ellipse
    ori_a = (perigee + apogee) / 2
    ori_c = (apogee - perigee) / 2
    ori_C = ori_c / proportion
    ori_b = math.sqrt(ori_a ** 2 - ori_c ** 2)

    # distorted ellipse
    a = ori_a
    b = ori_b / perspective
    c = math.sqrt(a**2 - b**2)
    y = b * math.sin(theta)
    x = a * math.cos(theta)
    X = x / proportion
    Y = y / proportion
    Pos = (Center[0] + ori_C + X,Center[1] + Y)
    RotPos = rotate_point_around(Center,Pos,inclination)
    if not behind_earth(RotPos,theta): pygame.draw.circle(screen,color,RotPos,1)

def draw_trajectory(perigee,apogee,inclination,color):
    for ang in range(0,360):
        draw_satellite(perigee,apogee,inclination,color,math.radians(ang))

def draw_trajectories():
    for i,row in data.iterrows():
        perigee = row['Perigee (km)'] + earthRadius
        apogee = row['Apogee (km)'] + earthRadius
        inclination = row['Inclination (degrees)']
        orbit = row['Class of Orbit']
        colors = {'LEO':yellow,'MEO':orange,'GEO':red,'Elliptical':blue}
        color = colors[orbit]
        draw_trajectory(perigee,apogee,inclination,color)

screen.blit(background,(0,0))
draw_trajectories()
pygame.display.update()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: running=False
