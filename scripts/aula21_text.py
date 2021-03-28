import pygame

red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

# inicializa o jogo e cria a janela
pygame.init()
# durante a inicialização do programa
pygame.font.init()

# cria uma janela com um tamanho fixo
screen = pygame.display.set_mode((800,600))

# criar uma fonte
comicsans = pygame.font.SysFont('Comic Sans MS',40)

# criar superfície textual
text = comicsans.render('Hello pygame',False,red)

# desenha texto na janela
screen.blit(text,(screen.get_width()/2-text.get_width()/2,screen.get_height()/2-text.get_height()/2))

# atualiza janela
pygame.display.update()

# responde a eventos (fechar)
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True