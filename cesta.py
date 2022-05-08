import pygame

class Cesta:
    def __init__(self, janela):
        self.janela = janela
        self.x = 320
        self.y = 352
        self.veloc = 6

    def move_cesta(self):
        keys = pygame.key.get_pressed() 
        if keys[pygame.K_LEFT] and self.x > -50: 
            self.x -= self.veloc         
    
        if keys[pygame.K_RIGHT] and self.x < 548: 
            self.x += self.veloc

    def inserir_cesta(self):
        imagem = pygame.image.load('cesta2.png')
        tam = 200, 150
        imagem = pygame.transform.scale(imagem, tam)
        self.janela.blit(imagem, (self.x, self.y))
