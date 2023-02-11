import pygame
import pandas as pd

white = (255,255,255)
red = (255,0,0)
black = (0,0,0)
green = (102,204,0)
blue=(0,0,255)
yellow=(230,220,50)
lightgray=(200,200,200)
cyan=(0,255,255)
purple=(128,0,128)
darkred=(140,0,0)

mk_color = {'blue':blue,'black':black,'red':red,'white':white,'yellow':yellow,'purple':purple,'lightgray':lightgray,'darkred':darkred,'cyan':cyan}

stats = pd.read_csv('../../dados/liverpool_2019.csv',usecols=['frame','bgcolor','play','player','x','y'])
plays = set(stats['play'])

# inicializa o jogo e cria a janela
pygame.init()
pygame.font.init()
font = pygame.font.SysFont('timesnewromanbold',40)
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
xoff = (screen.get_width()-width)/2
yoff = (screen.get_height()-height)/2

# jumps from the last frame of a play to the first frame of a new play
# goes around to the beginning of the dataframe for a continuous animation
def new_play():
    global frame, play, plays, pstats, maxframe
    frame=0
    if len(plays) == 0: plays = set(stats['play'])
    play = plays.pop()
    pstats = stats[stats['play']==play]
    maxframe = pstats['frame'].max()

new_play()

def draw_field():
        # desenha nome da jogada
        text = font.render(play,False,black)
        screen.blit(text,(screen.get_width()/2-text.get_width()/2,screen.get_height()/2-text.get_height()-height/2))
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

done = False
while not done:
    # responde a eventos (fechar)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # limpa ecrã
    screen.fill(green)
    draw_field()
    draw_frame()

    # atualiza janela
    pygame.display.update()
    # avança relógio
    clock.tick(fps)
    if frame<maxframe: frame+=1
    else: new_play()
