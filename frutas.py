import pygame
from random import randint

#cria classe das frutas
class Fruta:
    def __init__(self, janela, img, tx, ty):  #inicializa classe
        self.janela = janela  #qual aba será inserida
        self.img = img  #por qual imagem vai ser representada na tela
        self.tam = tx, ty  #tamanho da fruta
        self.score = 0  #quantas vezes a fruta é coletada

        #posição aleatória nos eixos x e y na qual será inserida
        self.x = randint(10, 470) 
        self.y = -(randint(10, 500))


    #movimento que as frutas realizarão na tela
    def movimento(self):

        #caso a fruta desapareça da tela pela parte de baixo é recolocada por cima em um ponto aleatório
        if self.y > 440:
            self.y = -(randint(10, 600))
            self.x = randint(10, 470)

        #enquanto permanecer na tela se movimenta com uma aceleração variável
        else:
            self.y += randint(9, 14)


    def inserir_fruta(self):
        imagem = pygame.image.load(self.img)  #carrega a imagem
        imagem = pygame.transform.scale(imagem, self.tam)  #ajusta tamanho da imagem
        self.janela.blit(imagem, (self.x, self.y))  #exibe na tela no local determinado


    def colisao(self, cesta):
        som_colisao = pygame.mixer.Sound('stomp.wav')  #carrega som da colisão

        #condição para contabilizar a colisão, caso colida
        if cesta.y <= self.y-10 <= 410 and cesta.x < self.x-30 and cesta.x+200 > self.x+60:
            self.score += 1  #contabiliza no score da fruta em questão
            som_colisao.play()  #som da colisão toca

            #fruta soma de tela e é recolocada em um ponto aleatório
            self.y = -(randint(10, 400))
            self.x = randint(10, 470)


    def reseta_score(melancia, uva, banana, laranja, morango):
        lista = [melancia, banana, uva, morango, laranja]
        for i in lista:  #reseta o score das frutas na lista uma por uma
            i.score = 0


    #chama as funções de inserir, movimento e colisão para cada fruta  
    def frutas_cesta_jogo(melancia, banana, uva, morango, laranja, cronometro, cesta):
        lista = [melancia, banana, uva, morango, laranja, cronometro]
        for i in lista:
            i.movimento()
            i.inserir_fruta()
            i.colisao(cesta)
        cesta.inserir_cesta()
        cesta.move_cesta()


    #exibe os scores de cada fruta na tela
    def insere_score(score_banana, score_uva, score_morango, score_laranja, score_melancia, janela, x=300):
        lista = [score_banana, score_uva, score_morango, score_laranja, score_melancia]
        for i in lista:
            janela.blit(i, (x, 470))
            x += 80