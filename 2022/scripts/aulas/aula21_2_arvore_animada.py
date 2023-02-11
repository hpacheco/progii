
import pygame
import math

green = (0,255,0)

pygame.init()
clock = pygame.time.Clock()
fps=1 # frames per second
screen = pygame.display.set_mode((600,600))

# uniao de dicionarios de listas
def uniao(d1,d2):
    d = d1.copy()
    for k in d2:
        if k in d: d[k] = d[k]+d2[k]
        else: d[k] = d2[k]
    return d

def tree(surface,i,n,pos,angle,width):
    if i < n:
        x,y = pos
        x1 = x + width * math.cos(angle)
        y1 = y - width * math.sin(angle)
        pos1 = x1,y1
        line = (pos,pos1,n//4)
        l = tree(surface,i+1,n,pos1,angle+math.pi/6,width/2)
        r = tree(surface,i+1,n,pos1,angle-math.pi/6,width/2)
        return uniao({i : [line]},uniao(l,r))
    else: return {}

start = (screen.get_width()/2,screen.get_height())
steps = tree(screen,0,20,start,math.pi/2,300)

done = False; frame=0
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: done = True

    if frame in steps:
        for pos1,pos2,sz in steps[frame]:
            pygame.draw.line(screen,green,pos1,pos2,width=sz)
        pygame.display.update()
    clock.tick(fps)
    frame+=1


