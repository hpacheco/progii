
import pygame
import math


# inicializa o jogo e cria a janela
pygame.init()

screen = pygame.display.set_mode((800,800))

angle = math.pi/4
width = 100
height = 50
w = width * math.cos(angle)
h = height * math.sin(angle)

# cor da relva à superfície
green=(0,135,46)
# profundidade e cor de cada camada de solo
layers = [('O',5,(0,0,0)),('A',25,(78,44,20)),('B',76,(90,0,0)),('C',122,(255,230,115)),('R',60,(50,50,50))]

offsets = sum([sz for x,sz,c in layers])
terrain = pygame.Surface((width*2,width+offsets))

# dá algum espaço em cima
offset = width
# desenha cada camada de solo
for n,t,c in layers:
    ps = [(0,offset),(width,offset),(width+w,offset-h),(width+w,offset-h+t),(width,offset+t),(0,offset+t)]
    pygame.draw.polygon(terrain,c,ps)
    offset +=t
# desenha camada de relva
ps = [(0,width),(width,width),(width+w,width-h),(0+w,width-h)]
pygame.draw.polygon(terrain,green,ps)

# ajusta terreno à janela
factor = terrain.get_width()/terrain.get_height()
terrain = pygame.transform.smoothscale(terrain,(int(screen.get_height()*factor),screen.get_height()))
# desenha terreno na janela
screen.blit(terrain,((screen.get_width()-terrain.get_width())/2,0))

# atualiza ecrã
pygame.display.update()

# responde a eventos (fechar)
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True


