import pygame
from random import randint
from tkinter import messagebox
from cesta import Cesta
from frutas import Fruta

pygame.init()

fundo = pygame.image.load('fundo1.png')
janela = pygame.display.set_mode((700,500))
time = 30

pygame.display.set_caption("Feira Maluca")

cesta = Cesta(janela)
melancia = Fruta(janela, 'melancia.png', randint(310, 470), -(randint(10, 150)), 60, 32)
banana = Fruta(janela, 'banana.png', randint(10, 270),-(randint(200, 500)), 60, 45)
uva = Fruta(janela, 'uva.png', randint(150, 320),-(randint(10, 800)), 60, 40)
morango = Fruta(janela, 'morango.png', randint(200, 370),-(randint(250, 600)), 50, 32)
laranja = Fruta(janela, 'laranja.png', randint(10, 70),-(randint(250, 700)), 60, 60)

font = pygame.font.Font('freesansbold.ttf', 32)

janela_aberta = True
while janela_aberta:
    time -= 0.05
    if time <= 0:
        messagebox.showinfo("Oops seu tempo acabou!", (f"Você conseguiu pegar:\nBananas: [x]\nUvas: [x]\nMorangos: [x]\nLaranjas: [x]\nMelancias: [x]"))
        if not messagebox.askyesno("Oops seu tempo acabou!", "Deseja jogar novamente?"):
            janela_aberta = False
        else:
            time = 30

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            janela_aberta = False

    janela.blit(fundo, (0, 0)) #inserir fundo 
    cesta.move_cesta()
    melancia.movimento()
    banana.movimento()
    uva.movimento()
    morango.movimento()
    laranja.movimento()
    
    cesta.inserir_cesta()
    melancia.inserir_fruta()
    banana.inserir_fruta()
    uva.inserir_fruta()
    morango.inserir_fruta()
    laranja.inserir_fruta()
    
    timer = font.render(str(int(time)), True, (255, 255, 255), None)
    janela.blit(timer, (40, 440))

    pygame.display.update()

pygame.quit()