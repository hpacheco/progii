import math
import pygame
import pandas as pd
import random

data = pd.read_excel('../dados/UCS-Satellite-Database-1-1-2021.xls',usecols=(8,11,12,14,15))
data.dropna(inplace=True)

red = (180,50,50)
green = (50,180,50)
yellow = (255, 255, 0)
orange = (255, 128, 0)
blue = (50, 50, 180)
black=(0,0,0)
transparent = (0,0,0,0)

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
clock = pygame.time.Clock(); fps=30 # frames per second

running = True

# make background
EarthWidth = int(EarthRadius * 2)
earth = pygame.transform.smoothscale(earth, (EarthWidth, EarthWidth))
earthRect = earth.get_rect()
earthRect.center = Center
background.blit(earth, earthRect)
empty = pygame.Surface((2,2),pygame.SRCALPHA)

class Satellite(pygame.sprite.Sprite):
    def __init__(self,perigee,apogee,inclination,color,theta,period):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((8,8),pygame.SRCALPHA)
        pygame.draw.circle(self.image, color,(0,0), 4)
        self.hidden = False
        self.rect = self.image.get_rect()
        self.color = color

        self.theta = theta
        self.period = math.radians(360 / period)
        self.inclination = inclination
        # original ellipse
        ori_a = (perigee + apogee) / 2
        ori_c = (apogee - perigee) / 2
        self.ori_C = ori_c / proportion
        ori_b = math.sqrt(ori_a ** 2 - ori_c ** 2)

        # distorted ellipse
        self.a = ori_a
        self.b = ori_b / perspective

    def update(self):
        self.theta = (self.theta + self.period) % (2*math.pi)
        y = self.b * math.sin(self.theta)
        x = self.a * math.cos(self.theta)
        X = x / proportion
        Y = y / proportion
        Pos = (Center[0] + self.ori_C + X, Center[1] + Y)
        RotPos = rotate_point_around(Center, Pos, self.inclination)
        if self.hidden:
            if not behind_earth(RotPos, self.theta):
                pygame.draw.circle(self.image, self.color, (0, 0), 4)
                self.hidden = False
        else:
            if behind_earth(RotPos,self.theta):
                self.image.fill(transparent)
                self.hidden = True
        self.rect.center = RotPos

    # initialize satellites
satellites = pygame.sprite.Group()
for i,row in data.iterrows():
    perigee = row['Perigee (km)'] + earthRadius
    apogee = row['Apogee (km)'] + earthRadius
    inclination = row['Inclination (degrees)']
    orbit = row['Class of Orbit']
    colors = {'LEO': yellow, 'MEO': orange, 'GEO': red, 'Elliptical': blue}
    color = colors[orbit]
    period = row['Period (minutes)']
    theta = random.uniform(0,2*math.pi)
    satellite = Satellite(perigee, apogee, inclination, color,theta,period)
    satellites.add(satellite)

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

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: running=False
    screen.blit(background, (0, 0))
    satellites.update()
    satellites.draw(screen)
    pygame.display.update()
    clock.tick(fps)
