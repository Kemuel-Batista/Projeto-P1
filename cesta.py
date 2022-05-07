import pygame

class Cesta:
    def __init__(self, janela, x=320, y=352):
        self.janela = janela
        self.x = x
        self.y = y 
        self.veloc = 15

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
