import pygame

white = (255,255,255)
grey = (128,128,128)
darkgrey = (64,64,64)
black = (0,0,0)

pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((600,600))
clock = pygame.time.Clock()
fps=30 # frames per second
font = pygame.font.Font(None,50)

done = False

class Button():
    def __init__(self,name):
        self.clicks = 0
        self.selected = False
        w = 200
        h = 50
        self.rect = pygame.Rect((screen.get_width() - w)/2,(screen.get_height()-h)/2,w,h)
        self.name = name
    def draw(self):
        pygame.draw.rect(screen,grey,self.rect)
        color = white if self.selected else darkgrey
        text = self.name if self.clicks == 0 else str(self.clicks) + ' clicks'
        txt = font.render(text,False,color)
        cx,cy = self.rect.center
        screen.blit(txt,(cx-txt.get_width()/2,cy-txt.get_height()/2))
    def hover(self,pos):
        self.selected = self.rect.collidepoint(pos)
    def click(self):
        if self.selected:
            self.clicks +=1

button = Button('Clicka-me')

while not done:
    # responde a eventos (fechar)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: done = True
        if event.type == pygame.MOUSEMOTION:
            button.hover(pygame.mouse.get_pos())
        if event.type == pygame.MOUSEBUTTONDOWN:
            button.click()

    button.draw()
    pygame.display.update(); clock.tick(fps)