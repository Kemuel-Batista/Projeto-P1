import pygame
from random import randint

class Fruta:
    def __init__(self, janela, img, x, y, tx, ty):
        self.janela = janela
        self.img = img
        self.x = x
        self.y = y 
        self.tam = tx, ty
        self.height = ty
        self.width = tx
        self.hitbox = (self.x, self.y, self.width, self.height)

    def movimento(self):
        if self.y > 700:
            self.y = -(randint(10, 800))
            self.x = randint(10, 470)
        else:
            self.y += randint(3, 11)

    def inserir_fruta(self, janela):
        imagem = pygame.image.load(self.img)
        imagem = pygame.transform.scale(imagem, self.tam)
        self.janela.blit(imagem, (self.x, self.y))

        self.hitbox = (self.x, self.y, self.width, self.height)
        pygame.draw.rect(janela, (0,0,0), self.hitbox, 1)

    def colisao(self, cesta, score):
        frutas = [[self.x, self.y],
                   [self.x+self.width, self.y],
                   [self.x, self.y+self.height],
                   [self.x+self.width, self.y+self.height]]

        for fruta in frutas:
            if cesta.x <= fruta[0] <= cesta.x+cesta.width\
                and cesta.y <= fruta[1] <= cesta.y+cesta.height:
                # destroi o item
                self.existes = False
                score += 1
        return -1