import pygame
from random import randint

class Fruta:
    def __init__(self, janela, img, x, y, tx, ty):
        self.janela = janela
        self.img = img
        self.x = x
        self.y = y 
        self.tam = tx, ty
        self.score = 0

    def movimento(self):
        if self.y > 440:
            self.y = -(randint(10, 800))
            self.x = randint(10, 470)
        else:
            self.y += randint(4, 11)

    def inserir_fruta(self):
        imagem = pygame.image.load(self.img)
        imagem = pygame.transform.scale(imagem, self.tam)
        self.janela.blit(imagem, (self.x, self.y))

    def colisao(self, cesta):
        som_colisao = pygame.mixer.Sound('stomp.wav')
        if self.y - 10 >= cesta.y and self.y <= 410:
            if (self.x - 30) > cesta.x and self.x + 60 < cesta.x + 200:
                self.score += 1
                self.y = -(randint(10, 800))
                self.x = randint(10, 470)
                som_colisao.play()

    def reseta_score(melancia, uva, banana, laranja, morango):
        uva.score = 0
        melancia.score = 0
        banana.score = 0
        laranja.score = 0 
        morango.score = 0