import pygame

# inicializa o jogo e cria a janela
pygame.init()

# cria uma janela com um tamanho fixo
screen = pygame.display.set_mode((800,800))

# carrega uma imagem de ficheiro
image = pygame.image.load('../../dados/python.png')

# pygame.transform.*

# inverte horizontalmente e/ou verticalmente
#image = pygame.transform.flip(image,False,True)
# redimensiona
#print(image.get_size())
#image = pygame.transform.scale(image,(100,100))
# redimensiona para o dobro do tamanho
#image = pygame.transform.scale2x(image)
# redimensiona com anti-aliasing
#image = pygame.transform.smoothscale(image,(800,800))
# roda com um ângulo em radianos
#image = pygame.transform.rotate(image,45)

# desenha a imagem no centro da janela
pos = (screen.get_width()/2-image.get_width()/2,screen.get_height()/2-image.get_height()/2)
screen.blit(image,pos)

# atualiza janela
pygame.display.update()

# responde a eventos (fechar)
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True