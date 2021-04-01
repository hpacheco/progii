import pygame
import pandas as pd

white = (255,255,255)
red = (255,0,0)
black = (0,0,0)
grey = (125,125,125)
green = (102,204,0)
blue=(0,0,255)
yellow=(230,220,50)
lightgray=(200,200,200)
cyan=(0,255,255)
purple=(128,0,128)
darkred=(140,0,0)

mk_color = {'blue':blue,'black':black,'red':red,'white':white,'yellow':yellow,'purple':purple,'lightgray':lightgray,'darkred':darkred,'cyan':cyan}

stats = pd.read_csv('../dados/liverpool_2019.csv',usecols=['frame','bgcolor','play','player','x','y'])
plays = list(set(stats['play']))
play = 0

# inicializa o jogo e cria a janela
pygame.init()
clock = pygame.time.Clock()
fps=30 # frames per second
proportion=6
width = 105*proportion; height = 68*proportion
meio = 9.15*proportion
garea_height = (16.5*2 + 7.32)*proportion
garea_width = 16.5*proportion
baliza_width = 1 * proportion
baliza_height = 7.32 * proportion
parea_height = 5.4864*2*proportion + baliza_height
parea_width = 5.4864 * proportion
screen = pygame.display.set_mode()
xoff = (screen.get_width()-width)/4
yoff = (screen.get_height()-height)/2
font = pygame.font.SysFont('timesnewromanbold',30)

# jumps from the last frame of a play to the first frame of a new play
# goes around to the beginning of the dataframe for a continuous animation
def change_play(i,fwd):
    global frame, play, plays, pstats, maxframe
    play+=i
    if play >= len(plays): play = 0
    if play < 0: play = len(plays)-1
    pstats = stats[stats['play'] == plays[play]]
    maxframe = pstats['frame'].max()
    frame = 0 if fwd else maxframe

change_play(1,True)

def draw_field():
        # dessenha framerate
        text = font.render(str(fps),False,black)
        screen.blit(text,(xoff+width/2-text.get_width()/2,(screen.get_height()-height)/2-text.get_height()))
        # desenha nomes das jogadas
        off = (screen.get_height()-30*len(plays))/2
        for i,p in enumerate(plays):
            color = black if i==play else grey
            text = font.render(p,False,color)
            screen.blit(text,(screen.get_width()/2+150,off))
            off +=30
        # desenha campo
        pygame.draw.rect(screen,white,pygame.Rect(xoff,yoff,width,height),width=2)
        pygame.draw.line(screen,white,(xoff+width/2,yoff),(xoff+width/2,yoff+height),width=2)
        pygame.draw.circle(screen,white,(xoff+width/2,yoff+height/2),meio,width=2)
        pygame.draw.rect(screen,white,pygame.Rect(xoff,yoff+(height-garea_height)/2,garea_width,garea_height),width=2)
        pygame.draw.rect(screen,white,pygame.Rect(xoff+width-garea_width,yoff+(height-garea_height)/2,garea_width,garea_height),width=2)
        pygame.draw.rect(screen,white,pygame.Rect(xoff,yoff+(height-parea_height)/2,parea_width,parea_height),width=2)
        pygame.draw.rect(screen,white,pygame.Rect(xoff+width-parea_width,yoff+(height-parea_height)/2,parea_width,parea_height),width=2)
        pygame.draw.rect(screen,white,pygame.Rect(xoff-baliza_width,yoff+(height-baliza_height)/2,baliza_width,baliza_height))
        pygame.draw.rect(screen,white,pygame.Rect(xoff+width,yoff+(height-baliza_height)/2,baliza_width,baliza_height))

def draw_frame():
    # sort invertido para a bola (player 0) aparecer no fim
    fstats = pstats[pstats['frame'] == frame].sort_values(by='player',ascending=False)
    for _,row in fstats.iterrows():
        x = row['x']
        y = row['y']
        color = black if row['player']==0 else mk_color[row['bgcolor']]
        sz = 3 if row['player']==0 else 8
        pygame.draw.circle(screen,color,(xoff+x*width/100,yoff+y*height/100),sz)

pause = False
done = False
while not done:
    # responde a eventos (fechar)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE: pause = not pause
            if event.key == pygame.K_UP: change_play(-1,fps >= 0)
            if event.key == pygame.K_DOWN: change_play(1,fps >= 0)
            if event.key == pygame.K_LEFT: fps -= 15
            if event.key == pygame.K_RIGHT: fps += 15

    if not pause:
        # limpa ecrã
        screen.fill(green)
        draw_field()
        draw_frame()

        # atualiza janela
        pygame.display.update()
        # avança relógio
        if fps > 0:
            if frame<maxframe: frame+=1
            else: change_play(1,True)
        elif fps < 0:
            if frame>0: frame-=1
            else: change_play(-1,False)
    clock.tick(abs(fps))
