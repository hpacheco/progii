import pygame
import math

red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
black = (0,0,0)

# inicializa o jogo e cria a janela
pygame.init()

# cria uma janela com um tamanho fixo
screen = pygame.display.set_mode((800,600))
screen.fill(black)

# cria um retângulo
# Rect(left,top,width,height,width=n)
box = pygame.Rect(100,200,200,100)
# desenha um retângulo
# rect(Surface,color,Rect,width=n)
pygame.draw.rect(screen,blue,box)
# desenha uma elipse dentro de um retângulo
# ellipse(Surface,color,Rect,width=n)
pygame.draw.ellipse(screen,green,box,width=3)
# desenha um arco
# arc(Surface,color,Rect,start,stop,with=n)
pygame.draw.arc(screen,red,box,math.pi/2,math.pi,width=2)

# bounding box de um cí­rculo
bbox = pygame.draw.circle(screen,red,(400,400),50)
print(bbox)
# bounding box de uma superfície
print(screen.get_rect())

# atualiza janela
pygame.display.update()

# responde a eventos (fechar)
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True