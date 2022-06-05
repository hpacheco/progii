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

perspective = 10
earthRadius = 6371
max_apogee = data['Apogee (km)'].max() + earthRadius

space = pygame.image.load('../dados/space.png')
background = pygame.Surface(space.get_size())
earth = pygame.image.load('../dados/earth.png')
screenX,screenY = background.get_size()
pygame.display.set_icon(earth)
screen = pygame.display.set_mode((screenX,screenY))
Center = (screenX/2,screenY/2)
clock = pygame.time.Clock(); fps=30 # frames per second

# adjust proportion to draw all satellites
min_screen = min(Center[0],Center[1])
proportion = max_apogee / min_screen
# round up to the hundreths
proportion = math.ceil (proportion / 100) * 100

show_l = True
show_m = True
show_g = True
show_e = True

running = True

# make background
def redraw_background():
    global background, earth, EarthRadius
    background.blit(space,(0,0))
    EarthRadius = earthRadius / proportion
    EarthWidth = int(EarthRadius * 2)
    newearth = pygame.transform.smoothscale(earth, (EarthWidth,EarthWidth))
    earthRect = newearth.get_rect()
    earthRect.center = Center
    background.blit(newearth,earthRect)

redraw_background()

class Satellite(pygame.sprite.Sprite):
    def __init__(self,perigee,apogee,inclination,color,theta,period,size):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((size*2,size*2),pygame.SRCALPHA)
        pygame.draw.circle(self.image,color,(0,0),size)
        self.hidden = False
        self.rect = self.image.get_rect()
        self.color = color
        self.size = size

        self.theta = theta
        self.period = math.radians(360 / period)
        self.inclination = inclination
        # original ellipse
        ori_a = (perigee + apogee) / 2
        self.ori_c = (apogee - perigee) / 2
        ori_b = math.sqrt(ori_a ** 2 - self.ori_c ** 2)

        # distorted ellipse
        self.a = ori_a
        self.b = ori_b / perspective

    def not_shown(self):
        if   self.color == yellow: return not show_l
        elif self.color == orange: return not show_m
        elif self.color == red   : return not show_g
        elif self.color == blue  : return not show_e

    def update(self):
        self.theta = (self.theta + self.period) % (2*math.pi)
        y = self.b * math.sin(self.theta)
        x = self.a * math.cos(self.theta)
        X = x / proportion
        Y = y / proportion
        Pos = (Center[0] + self.ori_c / proportion + X, Center[1] + Y)
        RotPos = rotate_point_around(Center, Pos, self.inclination)
        newhidden = self.not_shown() or behind_earth(RotPos, self.theta)
        if self.hidden:
            if not newhidden:
                pygame.draw.circle(self.image, self.color, (0, 0),self.size)
        else:
            if newhidden:
                self.image.fill(transparent)
        self.hidden = newhidden
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
    sizes = {'LEO': 1, 'MEO': 2, 'GEO': 3, 'Elliptical': 4}
    size = sizes[orbit]
    satellite = Satellite(perigee, apogee, inclination, color,theta,period,size)
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
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_MINUS:
                proportion += 100
                redraw_background()
            if event.key == pygame.K_PLUS:
                proportion = max(100,proportion-100)
                redraw_background()
            if event.key == pygame.K_LEFT:
                Center = (Center[0]+100,Center[1])
                redraw_background()
            if event.key == pygame.K_RIGHT:
                Center = (Center[0]-100,Center[1])
                redraw_background()
            if event.key == pygame.K_UP:
                Center = (Center[0],Center[1]+100)
                redraw_background()
            if event.key == pygame.K_DOWN:
                Center = (Center[0],Center[1]-100)
                redraw_background()
            if event.key == pygame.K_g:
                show_g = not show_g
            if event.key == pygame.K_l:
                show_l = not show_l
            if event.key == pygame.K_m:
                show_m = not show_m
            if event.key == pygame.K_e:
                show_e = not show_e

    screen.blit(background, (0, 0))
    satellites.update()
    satellites.draw(screen)
    pygame.display.update()
    clock.tick(fps)
