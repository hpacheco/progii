import pygame
import random
import math

white = (255,255,255)
black = (0,0,0)

# inicializa o jogo e cria a janela
pygame.init()
screen = pygame.display.set_mode((600,600))
clock = pygame.time.Clock()
fps=30 # frames per second

class Player():
    def __init__(self):
        self.width = 200
        self.height = 20
        self.px = 300
        self.py = 600-self.height/2
    def get_rect(self):
        return pygame.Rect(self.px - self.width / 2, self.py - self.height / 2, self.width, self.height)
    def move_to(self,px):
        self.px = px
        if self.px <= 100: self.px = 100
        if self.px >= 500: self.px = 500
    def move(self,d):
        self.move_to(self.px+d)
    def draw(self):
        pygame.draw.rect(screen,white,self.get_rect())

class Ball():
    def reset(self):
        angle = random.uniform(0,2*math.pi)
        self.vx = 5*math.cos(angle)
        self.vy = 5*math.sin(angle)
        self.px = 300
        self.py = 300
        self.radius = 20
    def get_rect(self):
        return pygame.Rect(self.px-self.radius,self.py-self.radius,self.radius*2,self.radius*2)
    def __init__(self):
        self.reset()
    def update(self):
        # atualiza velocidade
        self.px = self.vx + self.px
        self.py = self.vy + self.py
        # deteta colisões com paredes e chão
        if self.px <= self.radius:
            self.px = self.radius; self.vx = -self.vx
        if self.px >= 600 - self.radius:
            self.px = 600 - self.radius; self.vx = -self.vx
        if self.py <= self.radius:
            self.py = self.radius; self.vy = -self.vy
        if self.py >= 600 - self.radius:
            self.reset()
        # deteta colisões com jogador
        if self.get_rect().colliderect(player.get_rect()):
            self.vy = -self.vy

    def draw(self):
        pygame.draw.circle(screen,white,(self.px,self.py),self.radius)

ball = Ball()
player = Player()
done = False
while not done:
    # responde a eventos (fechar)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT: player.move(-20)
            if event.key == pygame.K_RIGHT: player.move(20)
        if event.type == pygame.MOUSEMOTION:
            x,y = pygame.mouse.get_pos()
            player.move_to(x)

    # atualiza posição
    ball.update()

    # limpa ecrã
    screen.fill(black)

    # desenha bola e barra
    ball.draw()
    player.draw()

    # atualiza janela e avança relógio
    pygame.display.update(); clock.tick(fps)
