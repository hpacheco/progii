import pygame

black = (0,0,0)
white = (255,255,255)

# inicializa o jogo e cria a janela
pygame.init()
clock = pygame.time.Clock()
fps=30 # frames per second
screen = pygame.display.set_mode()

# inicializa font
fontsize = int(min(screen.get_width()/2,screen.get_height()/2))
font = pygame.font.SysFont('timesnewromanbold',fontsize)

frame = 0
done = False
while not done:
    # limpa ecrã
    screen.fill(black)
    # responde a eventos (fechar)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: done = True
    # desenha frame
    text = font.render(str(frame // fps), False, white)
    textLeft = screen.get_width() / 2 - text.get_width() / 2
    textTop = screen.get_height() / 2 - text.get_height() / 2
    screen.blit(text,(textLeft,textTop))
    # atualiza janela
    pygame.display.update()
    # avança relógio
    clock.tick(fps)
    frame += 1