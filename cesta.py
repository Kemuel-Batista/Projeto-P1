import pygame

from frutas import Fruta

class Cesta:
    def __init__(self, janela, x=320, y=300):
        self.janela = janela
        self.x = x
        self.y = y 
        self.veloc = 6
        self.height = 150
        self.width = 200

        self.image = pygame.image.load('cesta2.png')
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.rect = self.image.get_rect()

    def move_cesta(self):
        keys = pygame.key.get_pressed() 
        if keys[pygame.K_LEFT] and self.x > -50: 
            self.x -= self.veloc         
    
        if keys[pygame.K_RIGHT] and self.x < 548: 
            self.x += self.veloc

    def inserir_cesta(self):
        self.janela.blit(self.image, (self.x, self.y))

    def colisao(self, fruta, score):
        corners = [[self.x, self.y],
                   [self.x+self.width, self.y],
                   [self.x, self.y+self.height],
                   [self.x+self.width, self.y+self.height]]
        
        # checa se qualquer um dos quatro cantos está dentro do jogador
        for corner in corners:
            if fruta.x <= corner[0] <= fruta.x+fruta.width\
                and fruta.y <= corner[1] <= fruta.y+fruta.height:
                # destroi o item
                fruta.existes = False
                score += 1
                return score