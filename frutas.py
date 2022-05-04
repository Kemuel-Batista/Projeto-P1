import pygame
from random import randint

class Fruta:
    def __init__(self, janela, img, x, y, tx, ty):
        self.janela = janela
        self.img = img
        self.x = x
        self.y = y 
        self.height = ty
        self.width = tx
        self.existes = True

        self.image = pygame.image.load(img)
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.rect = self.image.get_rect()

    def movimento(self):
        if self.y > 700:
            self.y = -(randint(10, 800))
            self.x = randint(10, 470)
        else:
            self.y += randint(3, 11)

    def inserir_fruta(self):
        self.janela.blit(self.image, (self.x, self.y))