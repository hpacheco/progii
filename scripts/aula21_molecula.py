
import pygame

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
lightblue = (60,90,100)
purple = (50,0,50)
darkgrey = (50,50,50)
lightgrey = (200,200,200)

# inicializa o jogo e cria a janela
pygame.init()

pygame.font.init()
font = pygame.font.SysFont('timesnewromanbold',20)

screen = pygame.display.set_mode()
screen.fill(white)

#posições de cada molécula
atoms = [(190,190,'H'),(190,325,'H'),(260,260,'N'),(390,260,'C'),(390,160,'H'),(390,390,'R'),(530,260,'C'),(630,350,'O'),(630,160,'O'),(660,40,'H')]
# ligações entre moléculas (utilizando índices)
ligands = {(0,2,'single'),(1,2,'single'),(2,3,'single'),(3,4,'single'),(3,5,'single'),(3,6,'single'),(6,7,'double'),(6,8,'single'),(8,9,'single')}
#formato de átomo
weights = {'H':('circle',25),'C':('circle',35),'N':('circle',45),'O':('circle',55),'R':('square',55)}
#cor de cada átomo
colors = {'H':lightblue,'N':purple,'C':darkgrey,'O':red,'R':lightgrey}

for i,j,tp in ligands:
   # draw ligands
   xi,yi,_ = atoms[i]
   xj,yj,_ = atoms[j]
   w = 2 if tp=='single' else 10
   pygame.draw.line(screen,black,(xi,yi),(xj,yj),width=w)

for x,y,name in atoms:
    # draw shapes
    tp,sz = weights[name]
    color = colors[name]
    if tp=='circle': pygame.draw.circle(screen,color,(x,y),sz)
    else: pygame.draw.rect(screen,color,pygame.Rect(x-sz/2,y-sz/2,sz,sz))
    # draw names
    text = font.render(name,False,white)
    screen.blit(text,(x-text.get_width()/2,y-text.get_height()/2))

# atualiza ecrã
pygame.display.update()

# responde a eventos (fechar)
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True


