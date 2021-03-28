import pygame

red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
black = (0,0,0)

# inicializa o jogo e cria a janela
pygame.init()

# cria uma janela com um tamanho fixo
screen = pygame.display.set_mode((800,600))
screen.fill(black)

# desenha um círculo
# circle(Surface,color,pos,radius,width=n)
pygame.draw.circle(screen,red,(200,200),50)
pygame.draw.circle(screen,red,(200,300),50,width=1)

# desenha um polígono
# polygon(Surface,color,pointlist,width=n)
pygame.draw.polygon(screen,green,[(200,200),(400,300),(300,400)])

# desenha uma linha
# line(Surface,color,start,end,width=n)
pygame.draw.line(screen,blue,(10,50),(30,100),width=10)

# copia a janela para o ícone
pygame.display.set_icon(screen)

# atualiza janela
pygame.display.update()

# responde a eventos (fechar)
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True