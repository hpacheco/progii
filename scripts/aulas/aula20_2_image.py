import pygame

# inicializa o jogo e cria a janela
pygame.init()

# cria uma janela com um tamanho fixo
screen = pygame.display.set_mode((800,600))

# carrega uma imagem de ficheiro
image = pygame.image.load('../../dados/python.png')

# altera o ícone da janela
pygame.display.set_icon(image)

# desenha a imagem no canto superior esquerdo da janela
#pos = (0,0)

# desenha a imagem quase no centro da janela
#pos = (screen.get_width()/2,screen.get_height()/2)

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