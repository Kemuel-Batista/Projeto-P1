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
        self.hitbox = (self.x, self.y, 90, 60)

    def move_cesta(self):
        keys = pygame.key.get_pressed() 
        if keys[pygame.K_LEFT] and self.x > -50: 
            self.x -= self.veloc         
    
        if keys[pygame.K_RIGHT] and self.x < 548: 
            self.x += self.veloc

    def inserir_cesta(self, janela):
        imagem = pygame.image.load('cesta2.png')
        tam = 200, 150
        imagem = pygame.transform.scale(imagem, tam)
        self.janela.blit(imagem, (self.x, self.y))

        self.hitbox = (self.x + 55, self.y + 60, 90, 50)
        pygame.draw.rect(janela, (0,0,0), self.hitbox, 1)