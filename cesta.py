import pygame

#cria classe da cesta (jogador)
class Cesta:
    def __init__(self, janela):  #inicializa classe
        self.janela = janela  #aba na qual será inserida
        #posição inicial na tela
        self.x = 320
        self.y = 352
        self.veloc = 14  #velocidade da cesta

    def move_cesta(self):
        keys = pygame.key.get_pressed()  #checa se as setas do teclado foram pressionadas

        #se a seta esquerda for pressionada e ainda tiver espaço esquerdo na tela, cesta se move
        if keys[pygame.K_LEFT] and self.x > -50: 
            self.x -= self.veloc         

        #se a seta direita for pressionada e ainda tiver espaço direito na tela, cesta se move
        if keys[pygame.K_RIGHT] and self.x < 548: 
            self.x += self.veloc


    #exibe imagem da cesta na tela
    def inserir_cesta(self):
        imagem = pygame.image.load('cesta2.png')  #carrega imagem da cesta
        tam = 200, 150  #tamanho da cesta
        imagem = pygame.transform.scale(imagem, tam)  #transforma o tamanho da imagem
        self.janela.blit(imagem, (self.x, self.y))  #exibe na tela
