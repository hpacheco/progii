
import pygame
import math

# inicializa o jogo e cria a janela
pygame.init()

screen = pygame.display.set_mode((600,600))

green = (0,255,0)

def tree(surface,n,pos,angle,width):
    if n > 0:
        x,y = pos
        x1 = x + width * math.cos(angle)
        y1 = y - width * math.sin(angle)
        pos1 = x1,y1
        pygame.draw.line(surface,green,pos,pos1,width=n//4)
        tree(surface,n-1,pos1,angle+math.pi/6,width/2)
        tree(surface,n-1,pos1,angle-math.pi/6,width/2)

start = (screen.get_width()/2,screen.get_height())
tree(screen,20,start,math.pi/2,300)

# atualiza ecrã
pygame.display.update()

# responde a eventos (fechar)
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True


