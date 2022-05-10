import pygame
from random import randint

class Fruta:
    def __init__(self, janela, img, tx, ty):
        self.janela = janela
        self.img = img
        self.x = randint(10, 470)
        self.y = -(randint(10, 500)) 
        self.tam = tx, ty
        self.score = 0

    def movimento(self):
        if self.y > 440:
            self.y = -(randint(10, 600))
            self.x = randint(10, 470)
        else:
            self.y += randint(6, 16)

    def inserir_fruta(self):
        imagem = pygame.image.load(self.img)
        imagem = pygame.transform.scale(imagem, self.tam)
        self.janela.blit(imagem, (self.x, self.y))

    def colisao(self, cesta):
        som_colisao = pygame.mixer.Sound('stomp.wav')
        if self.y - 10 >= cesta.y and self.y <= 410:
            if (self.x - 30) > cesta.x and self.x + 60 < cesta.x + 200:
                self.score += 1
                self.y = -(randint(10, 400))
                self.x = randint(10, 470)
                som_colisao.play()

    def aumenta_tmp(self, time):
        if self.score == 1:
            time += 15
            self.score = 0

    def reseta_score(melancia, uva, banana, laranja, morango):
        lista = [melancia, banana, uva, morango, laranja]
        for i in lista:
            i.score = 0

    def frutas_cesta_jogo(melancia, banana, uva, morango, laranja, cesta):
        lista = [melancia, banana, uva, morango, laranja]
        for i in lista:
            i.movimento()
            i.inserir_fruta()
            i.colisao(cesta)
        cesta.inserir_cesta()
        cesta.move_cesta()

    def insere_score(score_banana, score_uva, score_morango, score_laranja, score_melancia, janela, x=300):
        lista = [score_banana, score_uva, score_morango, score_laranja, score_melancia]
        for i in lista:
            janela.blit(i, (x, 470))
            x += 80