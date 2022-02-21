import pygame

# inicializa o jogo e cria a janela
pygame.init()

# cria uma janela com um tamanho fixo
screen = pygame.display.set_mode((800,600))

# uma cor RGB
blue=(0,0,255)
# altera a cor de fundo da janela
screen.fill(blue)
# altera o nome da janela
pygame.display.set_caption("window title")
# imprime tamanho da janela
print(screen.get_size())

# atualiza janela
pygame.display.update()

# responde a eventos (fechar)
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True