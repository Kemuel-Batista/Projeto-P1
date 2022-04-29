import pygame
from random import randint

class Fruta:
    def __init__(self, janela, img, x, y, tx, ty):
        self.janela = janela
        self.img = img
        self.x = x
        self.y = y 
        self.tam = tx, ty

    def movimento(self):
        if self.y > 700:
            self.y = -(randint(10, 800))
            self.x = randint(10, 470)
        else:
            self.y += randint(3, 11)

    def inserir_fruta(self):
        imagem = pygame.image.load(self.img)
        imagem = pygame.transform.scale(imagem, self.tam)
        self.janela.blit(imagem, (self.x, self.y))  